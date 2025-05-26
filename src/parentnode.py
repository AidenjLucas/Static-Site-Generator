from htmlnode import *

class ParentNode(HTMLNode):

    def __init__(self,tag,children,props=None): 
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode needs a tag")
        if self.children == None:
            raise ValueError("ParentNodes Child has no value")
        return f"<{self.tag}{self.props_to_html()}>" + combine_nodes(self,"") + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"  




def combine_nodes(node,final_string):
  
    if node.children == None or len(node.children) < 1:
        return final_string

    for child in node.children:
        combine_nodes(child,final_string)
        final_string += child.to_html()
        
    return final_string
 



 

