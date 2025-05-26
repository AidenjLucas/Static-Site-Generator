import unittest

from htmlnode import *

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

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})             
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div",[])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_mult_children(self):
        child_node2 = LeafNode("i", "child2")
        child_node1 = LeafNode("b", "child1")
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node,child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>child1</b><i>child2</i></div>")   

if __name__ == "__main__":
    unittest.main()


