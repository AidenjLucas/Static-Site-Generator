import unittest

from htmlnode import HTMLNode,LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p","test value",None,{"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.__repr__(),"HTMLNode(p, test value, children: None, {'href': 'https://www.google.com', 'target': '_blank'})")
        
    def test_props(self):
        node = HTMLNode("p","test value",None,{"href": "https://www.google.com","target": "props"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="props"')
    
    def test_no_props(self):
        node = HTMLNode("p","test value",[],None)
        self.assertEqual(node.props_to_html(),"")

    def test_leaf_to_html_p(self):  
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  


if __name__ == "__main__":
    unittest.main()