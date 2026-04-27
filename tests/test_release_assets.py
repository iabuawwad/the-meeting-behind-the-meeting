from pathlib import Path
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ReleaseAssetsTest(unittest.TestCase):
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
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "0.2.1")

    def test_readme_warns_against_source_zip_for_claude_install(self):
        readme = (ROOT / "README.md").read_text()
        self.assertIn("Do not download the GitHub source ZIP for Claude installation", readme)
        self.assertIn("the-meeting-behind-the-meeting-skill-v0.2.1.zip", readme)
        self.assertIn("the-meeting-behind-the-meeting-plugin-v0.2.1.zip", readme)

    def test_install_docs_include_release_asset_installation(self):
        install = (ROOT / "docs/INSTALL.md").read_text()
        self.assertIn("Install for normal users", install)
        self.assertIn("GitHub Releases ZIP assets", install)
        self.assertIn("Do not use Code -> Download ZIP unless you are a developer.", install)
        self.assertIn("the-meeting-behind-the-meeting-skill-v0.2.1.zip", install)
        self.assertIn("the-meeting-behind-the-meeting-plugin-v0.2.1.zip", install)


if __name__ == "__main__":
    unittest.main()
