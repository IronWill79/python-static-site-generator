import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        md = """
# Valid Title

content
"""
        title = extract_title(md)
        self.assertEqual(title, "Valid Title")

    def test_missing_title_raises_exception(self):
        md = "## Missing Title"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()
