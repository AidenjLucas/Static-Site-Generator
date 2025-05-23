import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p","test value",[],{"href": "https://www.google.com","target": "_blank","tree": "apple",})
        print(node)
        
    def test_props(self):
        node = HTMLNode("p","test value",[],{"href": "https://www.google.com","target": "_blank","tree": "apple",})
        print(node.props_to_html()) 
    
  


  


if __name__ == "__main__":
    unittest.main()