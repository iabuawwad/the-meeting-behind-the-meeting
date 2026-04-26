from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SkillFrontmatterTest(unittest.TestCase):
    def test_all_skill_files_have_required_name(self):
        skill_files = sorted(ROOT.glob("**/SKILL.md"))
        self.assertGreaterEqual(len(skill_files), 5)
        for path in skill_files:
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text()
                self.assertIn("name: the-meeting-behind-the-meeting", text)

    def test_all_skill_files_mention_transcript_quality_gate(self):
        skill_files = sorted(ROOT.glob("**/SKILL.md"))
        for path in skill_files:
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text().lower()
                self.assertIn("transcript quality gate", text)


if __name__ == "__main__":
    unittest.main()
