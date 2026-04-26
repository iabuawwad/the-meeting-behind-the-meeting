from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepoStructureTest(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            "README.md",
            "DESCRIPTION.md",
            "LICENSE",
            "CHANGELOG.md",
            "VERSION",
            "AGENTS.md",
            "CLAUDE.md",
            ".gitignore",
            "docs/INSTALL.md",
            "docs/USAGE.md",
            "docs/TESTING.md",
            "docs/VERSIONING.md",
            "docs/MODEL_ROUTING.md",
            "docs/RELEASE_CHECKLIST.md",
            ".github/workflows/validate.yml",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_version_is_semantic(self):
        version_file = ROOT / "VERSION"
        self.assertTrue(version_file.is_file())
        self.assertRegex(version_file.read_text().strip(), r"^\d+\.\d+\.\d+$")

    def test_claude_skill_paths_exist(self):
        self.assertTrue((ROOT / "skill/claude/SKILL.md").is_file())
        self.assertTrue((ROOT / ".claude/skills/the-meeting-behind-the-meeting/SKILL.md").is_file())

    def test_codex_skill_paths_exist(self):
        self.assertTrue((ROOT / "skill/codex/SKILL.md").is_file())
        self.assertTrue((ROOT / ".agents/skills/the-meeting-behind-the-meeting/SKILL.md").is_file())

    def test_cowork_plugin_wrapper_exists(self):
        required = [
            "skill/cowork-plugin/README.md",
            "skill/cowork-plugin/plugin.json",
            "skill/cowork-plugin/skills/the-meeting-behind-the-meeting/SKILL.md",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
