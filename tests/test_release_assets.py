from pathlib import Path
import os
import subprocess
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NAME = "the-meeting-behind-the-meeting"
VERSION = "0.2.2"


def zip_names(path):
    with zipfile.ZipFile(path) as archive:
        return archive.namelist()


class ReleaseAssetsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(["bash", "scripts/build-skill-zip.sh"], cwd=ROOT, check=True)
        subprocess.run(["bash", "scripts/build-plugin-zip.sh"], cwd=ROOT, check=True)

    def test_build_scripts_exist_and_are_executable(self):
        for script in [
            "scripts/build-skill-zip.sh",
            "scripts/build-plugin-zip.sh",
            "scripts/build-release-assets.sh",
        ]:
            path = ROOT / script
            with self.subTest(script=script):
                self.assertTrue(path.is_file())
                self.assertTrue(os.access(path, os.X_OK))

    def test_version_is_release_version(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), VERSION)

    def test_readme_warns_against_source_zip_for_claude_install(self):
        readme = (ROOT / "README.md").read_text()
        self.assertIn("Do not download the GitHub source ZIP for Claude installation", readme)
        self.assertIn(f"{NAME}-skill-v{VERSION}.zip", readme)
        self.assertIn(f"{NAME}-plugin-v{VERSION}.zip", readme)
        self.assertIn("Why the skill asks questions first", readme)

    def test_install_docs_include_release_asset_installation(self):
        install = (ROOT / "docs/INSTALL.md").read_text()
        self.assertIn("Install for normal users", install)
        self.assertIn("GitHub Releases ZIP assets", install)
        self.assertIn("Do not use Code -> Download ZIP unless you are a developer.", install)
        self.assertIn("Do not upload the GitHub source ZIP.", install)
        self.assertIn(f"{NAME}-skill-v{VERSION}.zip", install)
        self.assertIn(f"{NAME}-plugin-v{VERSION}.zip", install)

    def test_skill_zip_contains_one_skill_and_support_folders(self):
        names = zip_names(ROOT / "dist" / f"{NAME}-skill-v{VERSION}.zip")
        self.assertEqual(sum(path.endswith("/SKILL.md") for path in names), 1)
        for folder in ["frameworks", "templates", "references", "resources"]:
            with self.subTest(folder=folder):
                self.assertTrue(any(path.startswith(f"{NAME}/{folder}/") for path in names))

    def test_plugin_zip_contains_manifest_skill_and_support_folders(self):
        names = zip_names(ROOT / "dist" / f"{NAME}-plugin-v{VERSION}.zip")
        self.assertIn(f"{NAME}/.claude-plugin/plugin.json", names)
        self.assertIn(f"{NAME}/skills/{NAME}/SKILL.md", names)
        for folder in ["frameworks", "templates", "references", "resources"]:
            with self.subTest(folder=folder):
                self.assertTrue(any(path.startswith(f"{NAME}/skills/{NAME}/{folder}/") for path in names))

    def test_claude_facing_skills_define_interactive_runtime(self):
        for skill_path in [
            "skill/claude/SKILL.md",
            ".claude/skills/the-meeting-behind-the-meeting/SKILL.md",
            "skill/cowork-plugin/skills/the-meeting-behind-the-meeting/SKILL.md",
        ]:
            text = (ROOT / skill_path).read_text()
            with self.subTest(skill=skill_path):
                self.assertIn("Default mode is Interactive Deep Mode", text)
                self.assertIn("Intake Questions", text)
                self.assertIn("Transcript Quality Score: XX / 100", text)
                self.assertIn("Participant Context Notes", text)

    def test_templates_include_proceed_level_in_reliability_badge(self):
        for template in sorted((ROOT / "templates").glob("*.md")):
            text = template.read_text()
            with self.subTest(template=template.name):
                self.assertIn("## Reliability Badge", text)
                self.assertIn("Transcript Quality", text)
                self.assertIn("Reconstruction Confidence", text)
                self.assertIn("Sentiment/Tone Confidence", text)
                self.assertIn("Conversation Integrity", text)
                self.assertIn("Proceed Level", text)


if __name__ == "__main__":
    unittest.main()
