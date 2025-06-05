import unittest
from markdown_html import *
from htmlnode import *

class TestMarkdownToHTML(unittest.TestCase):
    
    def test_blocks_to_html(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )
    def test_codeblock(self):
        md = """
```This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
   
    def test_heading_block(self):
        md = "###### TREEHOUSE"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>TREEHOUSE</h6></div>",
        )

        
    '''def test_quoteblock(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )'''
    def test_unorderedblock(self):
        md = """
- Dog
- Cat
- Snake
- Rat
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ul><li>Dog</li><li>Cat</li><li>Snake</li><li>Rat</li></ul></div>",
            )
    
    def test_orderedblock(self):
        md = """
1. **Apples**
2. Oranges
3. Grapes
4. Blueberries
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ol><li><b>Apples</b></li><li>Oranges</li><li>Grapes</li><li>Blueberries</li></ol></div>",
            )
        


if __name__ == "__main__":
    unittest.main()