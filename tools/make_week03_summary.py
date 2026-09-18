"""Create a deterministic, readable Week 3 course summary image."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "Week03_Rule_QA_Summary.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

FONT_PATH = Path("C:/Windows/Fonts/msyh.ttc")
if not FONT_PATH.exists():
    FONT_PATH = Path("C:/Windows/Fonts/simhei.ttf")


def font(size: int, bold: bool = False):
    # Microsoft YaHei collection supports the Chinese text used in this card.
    return ImageFont.truetype(str(FONT_PATH), size, index=1 if bold else 0)


def wrap(draw, text, fnt, max_width):
    lines, current = [], ""
    for char in text:
        candidate = current + char
        if draw.textlength(candidate, font=fnt) > max_width and current:
            lines.append(current)
            current = char
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def draw_box(draw, xy, title, items, color):
    x, y, w, h = xy
    draw.rounded_rectangle((x, y, x + w, y + h), radius=22, fill="#ffffff", outline="#d9e2ec", width=3)
    draw.rectangle((x, y, x + 12, y + h), fill=color)
    draw.text((x + 30, y + 23), title, font=font(30, True), fill="#102a43")
    y_pos = y + 78
    body_font = font(23)
    for item in items:
        draw.ellipse((x + 32, y_pos + 8, x + 45, y_pos + 21), fill=color)
        lines = wrap(draw, item, body_font, w - 88)
        for line in lines:
            draw.text((x + 62, y_pos), line, font=body_font, fill="#243b53")
            y_pos += 31
        y_pos += 12


img = Image.new("RGB", (1600, 1120), "#f5f7fa")
draw = ImageDraw.Draw(img)
draw.rectangle((0, 0, 1600, 185), fill="#12355b")
draw.text((70, 42), "第 3 周：规则问答机器人", font=font(50, True), fill="#ffffff")
draw.text((74, 112), "个人实践 · rules.txt → Qwen → 回答 + 依据条款", font=font(28), fill="#d9eaf7")

# Flow strip
draw.rounded_rectangle((70, 220, 1530, 300), radius=18, fill="#e6f0fa")
flow = ["用户问题", "读取规则全文", "Qwen 判断", "Answer + Evidence"]
xs = [110, 470, 835, 1190]
for i, label in enumerate(flow):
    draw.text((xs[i], 244), label, font=font(27, True), fill="#12355b")
    if i < 3:
        draw.text((xs[i] + 235, 241), "→", font=font(34, True), fill="#2f80ed")

draw_box(draw, (70, 340, 710, 325), "课程要求", [
    "连续接收问题，输入 exit 退出",
    "回答使用与问题相同的语言",
    "必须显示规则编号和原文依据",
    "规则没有答案时明确说无法确认",
], "#2f80ed")
draw_box(draw, (820, 340, 710, 325), "本地已建立", [
    "week03_rule_chatbot/app.py",
    "rules.txt：翰林生活馆规则摘要与来源",
    ".env.example：不含密钥的配置模板",
    "4 项离线测试已通过",
], "#27ae60")
draw_box(draw, (70, 705, 710, 300), "三类验收题", [
    "电热水壶：应引用第 11 条及入住指南",
    "访客进房：应引用第 17 条",
    "打印机位置：规则没有答案，Evidence: Not found",
], "#f2994a")
draw_box(draw, (820, 705, 710, 300), "继续操作", [
    "打开同一个项目根目录，不要新建空仓库",
    "配置同地域 API Key 与 Base URL",
    "运行 --check、--test-api、三道问题",
    "确认 git status 没有 .env 后再提交",
], "#9b51e0")

draw.text((72, 1050), "项目根目录：C:\\Users\\31797\\Documents\\ChatGPT\\作业 3\\AI_Project_2026_2  ·  详见 HANDOFF.md 与 docs/status/Week03_STATUS.md", font=font(20), fill="#486581")
img.save(OUT, format="PNG", optimize=True)
print(OUT)
