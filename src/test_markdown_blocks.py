import unittest
from markdown_blocks import *


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_block_type_heading(self):
        markdown = "###### Heading 1"
        self.assertEqual(
            block_to_block_type(markdown),BlockType.HEADING)
    
    def test_markdown_to_block_type_heading_fail(self):
        markdown = "####### Heading 1"
        self.assertEqual(
            block_to_block_type(markdown),BlockType.PARAGRAPH)
        
    def test_markdown_to_block_type_code(self):
        markdown = "``` this is code```"
        
        self.assertEqual(
            block_to_block_type(markdown),BlockType.CODE)        
    
    def test_markdown_to_block_type_quote(self):
        markdown = "> we say\n> you say\n> cheese"
        
        self.assertEqual(
            block_to_block_type(markdown),BlockType.QUOTE)   
    
    def test_markdown_to_block_type_unordered(self):
        markdown = "- unordered list\n- 1\n- 2"
        
        self.assertEqual(
            block_to_block_type(markdown),BlockType.UNORDERED_LIST)   
    
    def test_markdown_to_block_type_ordered(self):
        markdown = "1. ordered list\n2. second\n3. third"
        
        self.assertEqual(
            block_to_block_type(markdown),BlockType.ORDERED_LIST)  
    
    

                 
if __name__ == "__main__":
    unittest.main()