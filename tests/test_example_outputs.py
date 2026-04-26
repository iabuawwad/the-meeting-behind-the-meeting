from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ExampleOutputsTest(unittest.TestCase):
    def test_expected_outputs_start_with_quality_assessment(self):
        required_prefixes = [
            "Transcript Quality Score:",
            "Reconstruction Confidence:",
            "Sentiment and Tone Confidence:",
            "Conversation Integrity:",
        ]
        outputs = sorted((ROOT / "examples/expected-outputs").glob("*.md"))
        self.assertEqual(len(outputs), 4)
        for path in outputs:
            with self.subTest(path=path.relative_to(ROOT)):
                lines = [line for line in path.read_text().splitlines() if line.strip()]
                self.assertGreaterEqual(len(lines), len(required_prefixes))
                for actual, prefix in zip(lines, required_prefixes):
                    self.assertTrue(actual.startswith(prefix), f"{actual!r} does not start with {prefix!r}")


if __name__ == "__main__":
    unittest.main()
