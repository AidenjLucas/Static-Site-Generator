import unittest
from copystatic import *


class TestMarkdownExtract(unittest.TestCase):

    def test_heading1(self):
        md = """
# This is a Heading

this is a paragraph text
"""
        extracted = extract_markdown(md)
        self.assertEqual(extracted,
                         "This is a Heading")
        
    def test_heading_exception(self):
        md = """
This is a Heading

this is a paragraph text
"""
        with self.assertRaises(Exception) as context:
            extract_markdown(md)
        self.assertEqual(str(context.exception), "No Header")

 
        
                         
if __name__ == "__main__":
    unittest.main()