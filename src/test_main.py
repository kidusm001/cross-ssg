import unittest
from main import *

class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello this is a man\n"
        title = extract_title(md)
        self.assertEqual("Hello this is a man", title)

    def test_extract_title_empty(self):
        md = ""
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertIn("No heading 1 found", str(context.exception))
    
    def test_extract_title_without(self):
        md = "Their is no title here.\nTheir is your mom here tho.\n"
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertIn("No heading 1 found", str(context.exception))

    def test_extract_title_other_headers(self):
        md = "## Their is no title here.\n#### Their is your mom here tho.\n"
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertIn("No heading 1 found", str(context.exception))

    def test_extract_title_whitespaces(self):
        md = "  # Hello world    "
        title = extract_title(md)
        self.assertEqual("Hello world", title)
    
    def test_extract_title_between(self):
        md = "Some other text\n# Title here\nMore text"
        title = extract_title(md)
        self.assertEqual("Title here", title)

    def test_extract_title_multi(self):
        md = "# first title\n# Title here\nMore text"
        title = extract_title(md)
        self.assertEqual("first title", title)

if __name__ == "__main__":
    unittest.main()
