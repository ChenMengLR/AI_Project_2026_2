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
        self.assertIn("전기포트", text)
        self.assertIn("[제17조 면회]", text)
        self.assertIn("택배물품은 지정된 장소에서 본인이 직접 수령해야 한다.", text)

    def test_prompt_contains_rules_and_question_but_not_credentials(self):
        prompt = app.build_prompt("[제1조]\n只允许测试", "测试问题")
        self.assertIn("只允许测试", prompt)
        self.assertIn("测试问题", prompt)
        self.assertNotIn("DASHSCOPE_API_KEY", prompt)
        self.assertIn("same language", app.SYSTEM_INSTRUCTIONS)
        self.assertIn("Never replace a relevant sentence with ellipses", app.SYSTEM_INSTRUCTIONS)

    def test_ask_uses_qwen_and_returns_model_text(self):
        client = Mock()
        client.chat.completions.create.return_value.choices = [
            Mock(message=Mock(content="Answer: 不可以。\nEvidence: 제11조")
        )]
        result = app.ask(client, "[제11조]\n전기포트는 사용할 수 없다.", "可以使用吗？", "qwen3.8-flash")
        self.assertIn("Evidence: 제11조", result)
        kwargs = client.chat.completions.create.call_args.kwargs
        self.assertEqual(kwargs["model"], "qwen3.8-flash")
        self.assertEqual(kwargs["extra_body"], {"enable_thinking": False})
        self.assertIn("可以使用吗？", kwargs["messages"][1]["content"])

    def test_visitor_answer_retains_every_condition_from_article_17(self):
        rules = app.read_rules(WEEK / "rules.txt")
        client = Mock()
        client.chat.completions.create.return_value.choices = [
            Mock(message=Mock(content="Answer: 朋友不能进房间。\nEvidence: 第17条。"))
        ]
        result = app.ask(client, rules, "朋友可以来我的房间吗？", "qwen3.8-flash")
        for required in ("行政支援室", "10:00–20:00", "指定地点", "不能进入", "[제17조 면회]", "행정지원실에 신청해야 한다"):
            self.assertIn(required, result)
        client.chat.completions.create.assert_called_once()

    def test_kettle_answer_retains_health_exception_from_source(self):
        rules = app.read_rules(WEEK / "rules.txt")
        client = Mock()
        client.chat.completions.create.return_value.choices = [
            Mock(message=Mock(content="Answer: 不可以使用电热水壶。\nEvidence: 第11条。"))
        ]
        result = app.ask(client, rules, "我可以在房间里使用电热水壶吗？", "qwen3.8-flash")
        for required in ("禁止携带或使用", "健康原因", "事先咨询行政支援室", "[제11조", "건강상 필요한 제품은"):
            self.assertIn(required, result)
        client.chat.completions.create.assert_called_once()

    def test_source_guards_do_not_change_unrelated_questions(self):
        rules = app.read_rules(WEEK / "rules.txt")
        model_answer = "Answer: 规则中没有购买地点。\nEvidence: Not found"
        self.assertEqual(
            app.ground_chinese_kettle_answer(rules, "电热水壶在哪里买？", model_answer),
            model_answer,
        )
        self.assertEqual(
            app.ground_chinese_visit_answer(rules, "朋友的房间有打印机吗？", model_answer),
            model_answer,
        )

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
