from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def public_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if relative.parts[0] in {".git", "tests"}:
            continue
        if "__pycache__" in relative.parts:
            continue
        if path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".txt"} or path.name in {
            "VERSION",
            "LICENSE",
        }:
            yield path


class RequiredDocsTest(unittest.TestCase):
    def test_required_public_docs_exist(self):
        required = [
            "README.md",
            "DESCRIPTION.md",
            "docs/INSTALL.md",
            "docs/USAGE.md",
            "docs/TESTING.md",
        ]
        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_no_unsafe_banned_phrases_in_public_content(self):
        banned = [
            "mind" + " reading",
            "detect" + " lies",
            "diagnose" + " personality",
            "guaranteed" + " emotion" + " detection",
            "psychological" + " diagnosis",
        ]
        failures = []
        for path in public_text_files():
            text = path.read_text(errors="ignore").lower().replace("-", " ")
            for phrase in banned:
                if phrase in text:
                    failures.append(f"{path.relative_to(ROOT)}: {phrase}")
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
