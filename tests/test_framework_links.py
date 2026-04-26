from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class FrameworkLinksTest(unittest.TestCase):
    def test_required_framework_files_exist(self):
        expected = [ROOT / "frameworks" / f"{index:02d}-{name}.md" for index, name in [
            (0, "transcript-quality-gate"),
            (1, "transcript-classification"),
            (2, "evidence-confidence-standard"),
            (3, "factual-reconstruction"),
            (4, "decision-accountability"),
            (5, "risk-register"),
            (6, "said-vs-meant"),
            (7, "communication-style"),
            (8, "trust-behaviour-prediction"),
            (9, "influence-participation"),
            (10, "culture-psychological-safety"),
            (11, "voice-tone-presence"),
            (12, "nonverbal-behavioural-signals"),
            (13, "next-meeting-playbook"),
        ]]
        missing = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
        self.assertEqual(missing, [])

    def test_codex_skill_resource_links_exist(self):
        skill = ROOT / "skill/codex/SKILL.md"
        text = skill.read_text()
        links = re.findall(r"`((?:frameworks|references|templates)/[^`]+)`", text)
        self.assertGreater(links, [])
        missing = [link for link in links if not (ROOT / link).is_file()]
        self.assertEqual(missing, [])

    def test_templates_contain_reliability_badge_fields(self):
        fields = [
            "Transcript Quality",
            "Reconstruction Confidence",
            "Sentiment/Tone Confidence",
            "Conversation Integrity",
        ]
        template_files = sorted((ROOT / "templates").glob("*.md"))
        self.assertGreaterEqual(len(template_files), 12)
        for path in template_files:
            text = path.read_text()
            with self.subTest(path=path.relative_to(ROOT)):
                for field in fields:
                    self.assertIn(field, text)


if __name__ == "__main__":
    unittest.main()
