"""Show a real app.py subprocess for recording; credentials remain inherited only."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import queue
import subprocess
import sys
import threading
import time
import tkinter as tk
from PIL import Image, ImageOps, ImageTk


PROJECT = Path(__file__).resolve().parents[1]
WORK = PROJECT / "week02_photo_classifier" / "runtime" / "demo"
WORK.mkdir(parents=True, exist_ok=True)
BG, PANEL, BORDER = "#0d1628", "#152238", "#28405c"
TEXT, MUTED, BLUE, GREEN = "#edf5ff", "#a8bdd4", "#78caff", "#69e2b1"


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class LiveDemo:
    def __init__(self, root: tk.Tk, project: Path, preview_only: bool):
        self.root, self.project, self.preview_only = root, project, preview_only
        self.course = project / "week02_photo_classifier"
        self.photos = []
        self.events = queue.Queue()
        self.process = None
        self.started = False
        self.started_utc = None
        self.timer = None
        self.stdout_lines = []
        self.exit_code = None
        self.report = None
        self.signals = {kind: WORK / f"ai-demo-{kind}.{suffix}" for kind, suffix in
                        (("start", "flag"), ("complete", "json"), ("ready", "json"))}
        root.title("AI Week02 Live Demo")
        root.geometry("1280x720+60+60")
        root.resizable(False, False)
        root.configure(bg=BG)
        root.tk.call("tk", "scaling", 1.0)
        root.protocol("WM_DELETE_WINDOW", self.close)
        self.label(root, "AI 第 2 周  ·  Qwen 照片分类", 23, TEXT, bold=True).place(x=22, y=15)
        self.label(root, "WANG HAOBIN  /  5 张课堂样例 + 2 张公开授权新素材", 12, MUTED).place(x=24, y=51)
        self.badge = self.label(root, "PREVIEW ONLY" if preview_only else "等待开始 · 不显示密钥", 13, BLUE, bold=True)
        self.badge.place(x=890, y=29, width=365)
        input_frame = self.box(root, 22, 84, 1236, 176)
        self.label(input_frame, "01   input/ · 本次全部输入图片", 13, BLUE, bold=True).place(x=12, y=7)
        images = sorted(p for p in (self.course / "input").iterdir()
                        if p.is_file() and p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"))
        for index, path in enumerate(images):
            x = 12 + index * 174
            self.photo(input_frame, path, x, 33, 161, 101)
            self.label(input_frame, path.name, 11, TEXT).place(x=x, y=137, width=161)
        command_frame = self.box(root, 22, 273, 1236, 67)
        self.label(command_frame, "02   实际执行命令  ·  使用项目 .venv 的 Python", 12, BLUE, bold=True).place(x=12, y=6)
        self.label(command_frame, "python -u app.py", 19, TEXT, font="Consolas", bold=True).place(x=14, y=27)
        self.label(command_frame, "工作目录：AI_Project_2026_2 / week02_photo_classifier", 11, MUTED).place(x=383, y=34)
        log_frame = self.box(root, 22, 353, 662, 300)
        self.label(log_frame, "03   子进程真实终端输出 · 逐行显示", 13, BLUE, bold=True).place(x=12, y=8)
        self.log = tk.Text(log_frame, bg=PANEL, fg=TEXT, insertbackground=TEXT,
                           borderwidth=0, highlightthickness=0, font=("Microsoft YaHei UI", 11),
                           wrap="word", state="disabled", spacing1=2, spacing3=2)
        self.log.place(x=12, y=40, width=638, height=246)
        self.output_frame = self.box(root, 697, 353, 561, 300)
        self.label(self.output_frame, "04   sorted/ · 本次实际分类副本", 13, BLUE, bold=True).place(x=12, y=8)
        self.output_hint = self.label(self.output_frame, "等待真实请求完成后读取文件", 12, MUTED)
        self.output_hint.place(x=12, y=118, width=536)
        self.status = self.label(root, "准备就绪：输入照片保持原文件；每次运行都会实际请求 Qwen。", 12, MUTED)
        self.status.place(x=24, y=665, width=1230)
        self.label(root, "这是助手执行的真实程序演示；新增图为公开授权素材，非本人摄影。", 10, MUTED).place(x=24, y=695)
        if not preview_only:
            self.signals["complete"].unlink(missing_ok=True)
        root.update_idletasks()
        write_json(self.signals["ready"], {"window_title": "AI Week02 Live Demo", "pid": os.getpid(),
                   "client_size": [1280, 720], "input_count": len(images), "preview_only": preview_only,
                   "ready_utc": datetime.now(timezone.utc).isoformat()})
        root.after(150, self.tick)

    def label(self, parent, text, size, color, bold=False, font="Microsoft YaHei UI"):
        return tk.Label(parent, text=text, font=(font, size, "bold" if bold else "normal"),
                        bg=parent.cget("bg"), fg=color, anchor="w")

    def box(self, parent, x, y, width, height):
        frame = tk.Frame(parent, bg=PANEL, highlightthickness=1, highlightbackground=BORDER)
        frame.place(x=x, y=y, width=width, height=height)
        return frame

    def photo(self, parent, path, x, y, width, height):
        with Image.open(path) as source:
            # A display thumbnail only; no input file is edited or replaced.
            thumb = ImageOps.contain(ImageOps.exif_transpose(source).convert("RGB"), (width, height))
            image = ImageTk.PhotoImage(thumb)
        self.photos.append(image)
        tk.Label(parent, image=image, bg="#0b1424", borderwidth=0).place(x=x, y=y, width=width, height=height)

    def append_log(self, line):
        self.stdout_lines.append(line)
        self.log.configure(state="normal")
        self.log.insert("end", line)
        self.log.see("end")
        self.log.configure(state="disabled")

    def start(self):
        self.started = True
        self.started_utc = datetime.now(timezone.utc)
        self.timer = time.monotonic()
        self.badge.configure(text="● 正在真实调用 Qwen", fg=GREEN)
        self.append_log("> python -u app.py\n")
        environment = os.environ.copy()
        environment["PYTHONUTF8"] = "1"
        environment["PYTHONUNBUFFERED"] = "1"
        self.process = subprocess.Popen([sys.executable, "-u", str(self.course / "app.py")],
            cwd=self.course, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding="utf-8", errors="replace", bufsize=1,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))

        def read_process():
            for line in self.process.stdout:
                self.events.put(("line", line))
            self.events.put(("exit", self.process.wait()))
        threading.Thread(target=read_process, daemon=True).start()

    def finished(self, code):
        self.exit_code = code
        elapsed = time.monotonic() - self.timer
        self.badge.configure(text=f"执行结束 · 退出码 {code}", fg=GREEN if code == 0 else "#ffbc77")
        report_path = self.course / "runtime" / "last_run.json"
        try:
            report = json.loads(report_path.read_text(encoding="utf-8"))
            if datetime.fromisoformat(report["started_utc"]) < self.started_utc:
                raise ValueError("stale report")
            self.report = report
            self.output_hint.destroy()
            for index, row in enumerate(report["images"]):
                x, y = 12 + (index % 4) * 136, 39 + (index // 4) * 120
                target = self.course / row.get("output", "unavailable")
                if row["status"] == "success" and target.is_file():
                    self.photo(self.output_frame, target, x, y, 127, 71)
                    self.label(self.output_frame, row["label"], 11, GREEN, bold=True).place(x=x, y=y+73, width=128)
                    self.label(self.output_frame, row["filename"], 8, MUTED).place(x=x, y=y+92, width=128)
                else:
                    self.label(self.output_frame, "失败 · 无分类副本", 10, "#ffbc77").place(x=x, y=y+30, width=127)
            total_tokens = sum(row.get("usage", {}).get("total_tokens") or 0 for row in report["images"])
            summary = (f"真实结果：成功 {report['success_count']} / 失败 {report['failure_count']}  ·  "
                       f"耗时 {elapsed:.1f} 秒  ·  本轮 {total_tokens:,} tokens  ·  输入原图保留")
            self.status.configure(text=summary, fg=GREEN)
        except (OSError, ValueError, KeyError, TypeError):
            self.status.configure(text=f"执行结束，退出码 {code}；未获得可确认属于本轮的结果记录。", fg="#ffbc77")
        self.root.after(10000, self.mark_complete)

    def mark_complete(self):
        write_json(self.signals["complete"], {
            "started_utc": self.started_utc.isoformat(),
            "completed_utc": datetime.now(timezone.utc).isoformat(),
            "exit_code": self.exit_code,
            "run_id": self.report.get("run_id") if self.report else None,
            "success_count": self.report.get("success_count") if self.report else None,
            "failure_count": self.report.get("failure_count") if self.report else None,
            "stdout_sha256": hashlib.sha256("".join(self.stdout_lines).encode("utf-8")).hexdigest(),
            "result_held_seconds": 10,
        })

    def tick(self):
        if not self.preview_only and not self.started and self.signals["start"].exists():
            self.start()
        while not self.events.empty():
            kind, value = self.events.get_nowait()
            if kind == "line":
                self.append_log(value)
            else:
                self.finished(value)
        if self.started and self.exit_code is None:
            self.status.configure(text=f"真实请求进行中 · 已用时 {time.monotonic()-self.timer:.1f} 秒 · 终端输出直接来自 app.py")
        self.root.after(100, self.tick)

    def close(self):
        if self.process is not None and self.process.poll() is None:
            self.process.terminate()
        self.root.destroy()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=PROJECT)
    parser.add_argument("--preview-only", action="store_true", help="Show inputs without starting an API subprocess")
    args = parser.parse_args()
    root = tk.Tk()
    LiveDemo(root, args.project, args.preview_only)
    root.mainloop()


if __name__ == "__main__":
    main()
