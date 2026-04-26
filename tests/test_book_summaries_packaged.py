from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

BOOK_SUMMARY_FILES = [
    "julius_fast_body_language_reference_guide.md",
    "kate_davis_body_language_reference_guide.md",
    "people_styles_at_work_and_beyond_reference_guide.md",
    "sizing_people_up_reference_guide.md",
    "its_the_way_you_say_it_reference_guide.md",
    "influence_and_persuasion_reference_guide.md",
    "the_culture_code_reference_guide.md",
    "what_every_body_is_saying_reference_guide.md",
]

PACKAGED_SKILL_LOCATIONS = [
    "skill/claude",
    "skill/codex",
    "skill/cowork-plugin/skills/the-meeting-behind-the-meeting",
    ".claude/skills/the-meeting-behind-the-meeting",
    ".agents/skills/the-meeting-behind-the-meeting",
]

RAW_BOOK_SUFFIXES = {".pdf", ".epub", ".azw3", ".mobi"}


class BookSummariesPackagedTest(unittest.TestCase):
    def test_canonical_book_summaries_exist(self):
        root = ROOT / "resources/book-summaries"
        self.assertTrue(root.is_dir())
        self.assertTrue((root / "README.md").is_file())
        missing = [name for name in BOOK_SUMMARY_FILES if not (root / name).is_file()]
        self.assertEqual(missing, [])

    def test_packaged_skill_locations_include_book_summaries(self):
        for location in PACKAGED_SKILL_LOCATIONS:
            with self.subTest(location=location):
                packaged = ROOT / location / "resources/book-summaries"
                self.assertTrue(packaged.is_dir())
                self.assertTrue((packaged / "README.md").is_file())
                missing = [name for name in BOOK_SUMMARY_FILES if not (packaged / name).is_file()]
                self.assertEqual(missing, [])

    def test_no_raw_book_formats_are_included(self):
        raw_files = [
            str(path.relative_to(ROOT))
            for path in ROOT.rglob("*")
            if path.is_file() and path.suffix.lower() in RAW_BOOK_SUFFIXES
        ]
        self.assertEqual(raw_files, [])

    def test_all_skill_files_reference_book_summaries(self):
        skill_files = sorted(ROOT.glob("**/SKILL.md"))
        self.assertGreaterEqual(len(skill_files), 5)
        missing_reference = []
        for path in skill_files:
            if "resources/book-summaries/" not in path.read_text():
                missing_reference.append(str(path.relative_to(ROOT)))
        self.assertEqual(missing_reference, [])


if __name__ == "__main__":
    unittest.main()
