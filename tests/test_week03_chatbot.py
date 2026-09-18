import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "week03_rule_chatbot"
sys.path.insert(0, str(WEEK))
import app  # noqa: E402


class Week03ChatbotTests(unittest.TestCase):
    def test_rules_are_utf8_and_contain_required_cases(self):
        text = app.read_rules(WEEK / "rules.txt")
        self.assertIn("电热水壶", text)
        self.assertIn("第17条 会客", text)
        self.assertIn("打印机位置与费用", text)

    def test_prompt_contains_rules_and_question_but_not_credentials(self):
        prompt = app.build_prompt("[第1条]\n只允许测试", "测试问题")
        self.assertIn("只允许测试", prompt)
        self.assertIn("测试问题", prompt)
        self.assertNotIn("DASHSCOPE_API_KEY", prompt)

    def test_ask_uses_qwen_and_returns_model_text(self):
        client = Mock()
        client.chat.completions.create.return_value.choices = [
            Mock(message=Mock(content="Answer: 不可以。\nEvidence: 第11条")
        )]
        result = app.ask(client, "[第11条]\n电热水壶不得使用。", "可以使用吗？", "qwen3.8-flash")
        self.assertIn("Evidence: 第11条", result)
        kwargs = client.chat.completions.create.call_args.kwargs
        self.assertEqual(kwargs["model"], "qwen3.8-flash")
        self.assertEqual(kwargs["extra_body"], {"enable_thinking": False})
        self.assertIn("可以使用吗？", kwargs["messages"][1]["content"])

    def test_missing_config_never_prints_key(self):
        with tempfile.TemporaryDirectory() as temp:
            env = Path(temp) / ".env"
            env.write_text("DASHSCOPE_API_KEY=secret-value\n", encoding="utf-8")
            key, base_url, _ = app.load_settings(env)
            self.assertEqual(key, "secret-value")
            self.assertEqual(base_url, "")
            with self.assertRaises(RuntimeError):
                app.create_client(key, base_url)


if __name__ == "__main__":
    unittest.main()
