import unittest
from textnode import TextNode,TextType
from inline_markdown import split_nodes_delimiter

class TestMarkDownToTextNode(unittest.TestCase):

    
        def test_delim_bold_and_italic(self):
            node = TextNode("**bold** and _italic_", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
            new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
            self.assertListEqual(
                [
                    TextNode("bold", TextType.BOLD),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                ],
                new_nodes,
            )

        def test_code_delim(self):
            node = TextNode("This is text with a `code block` word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertListEqual(new_nodes,[
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                            ])
            
        def test_bold_delim(self):
            node = TextNode("This is text with a **code block** word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
            self.assertListEqual(new_nodes,[
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.BOLD),
                            TextNode(" word", TextType.TEXT),
                            ])
            
        def test_multiple_nodes(self):
            node = TextNode("This is text with a **code block** word", TextType.TEXT)
            node1 = TextNode("This is text with all **code block two** words", TextType.TEXT)
            node2 = TextNode("'This is Code'", TextType.CODE)
            new_nodes = split_nodes_delimiter([node,node1,node2], "**", TextType.BOLD)
            self.assertListEqual(new_nodes,[
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.BOLD),
                            TextNode(" word", TextType.TEXT),
                            TextNode("This is text with all ", TextType.TEXT),
                            TextNode("code block two", TextType.BOLD),
                            TextNode(" words", TextType.TEXT),
                            TextNode("'This is Code'", TextType.CODE),
                            ])
            
        def test_no_match_delim(self):
            node = TextNode("This is text with a **code block word", TextType.TEXT)
            with self.assertRaises(Exception) as context:
                split_nodes_delimiter([node], "**", TextType.BOLD)
            self.assertEqual(str(context.exception), "Invalid Markdown Syntax")
    
        def test_delim_bold_double(self):
            node = TextNode(
                "This is text with a **bolded** word and **another**", TextType.TEXT
            )
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
            self.assertListEqual(
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("bolded", TextType.BOLD),
                    TextNode(" word and ", TextType.TEXT),
                    TextNode("another", TextType.BOLD),
                ],
                new_nodes,
            )

        def test_delim_bold_multiword(self):
            node = TextNode(
                "This is text with a **bolded word** and **another**", TextType.TEXT
            )
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
            self.assertListEqual(
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("bolded word", TextType.BOLD),
                    TextNode(" and ", TextType.TEXT),
                    TextNode("another", TextType.BOLD),
                ],
                new_nodes,
            )

        def test_delim_italic(self):
            node = TextNode("This is text with an _italic_ word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word", TextType.TEXT),
                ],
                new_nodes,
            )
      
