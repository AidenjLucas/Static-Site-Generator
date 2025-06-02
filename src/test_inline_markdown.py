import unittest
from textnode import TextNode,TextType
from inline_markdown import *

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
      
        def test_extract_markdown_images(self):
            matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
        def test_extract_markdown_links(self):
            matches = extract_markdown_links(
            ("This is text with a link [to boot dev](https://www.boot.dev) "
            "and [to youtube](https://www.youtube.com/@bootdotdev)")
            )
            self.assertListEqual([("to boot dev", "https://www.boot.dev"),
                                ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
        
        def test_extract_markdown_image_wrong_func(self):
            matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertNotEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
        def test_split_images(self):
            node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode(
                        "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                    ),
                ],
                new_nodes,
            )

        def test_split_links(self):
            node = TextNode(
                "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode(
                        "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                    ),
                ],
                new_nodes,
            )

        def test_split_image_single(self):
            node = TextNode(
                "![image](https://www.example.COM/IMAGE.PNG)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
                ],
                new_nodes,
            )

        def test_text_to_textnodes(self):



            text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            nodes = text_to_textnodes(text)
            self.assertListEqual(
                [
                    
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                    
                ],
                nodes,
            )

if __name__ == "__main__":
    unittest.main()