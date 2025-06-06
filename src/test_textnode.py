import unittest
from textnode import TextNode,TextType,text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq_all(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text", TextType.BOLD, "https://www.bootdev.dev")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD,"http://ww.bootdev.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.bootdev.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_img(self):
        node = TextNode("This is a img node", TextType.IMAGE,"http://ww.bootdev.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), '<img src="http://ww.bootdev.dev" alt="This is a img node"></img>')

    def test_link(self):    
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="None">This is a link node</a>')
        
    def test_error_tag(self):
        node = TextNode("This is a link node", "noType")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "invalid text type: noType")


if __name__ == "__main__":
    unittest.main()