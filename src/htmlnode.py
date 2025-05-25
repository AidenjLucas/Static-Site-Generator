

class HTMLNode():

   def __init__(self, tag=None, value=None, children=None, props=None):
      self.tag = tag
      self.value = value
      self.children = children 
      self.props = props

   def to_html(self):
      raise NotImplementedError("to_html has not been implemented")
   
   def props_to_html(self):
      if self.props == None:
          return ""
      return "".join(map(lambda item: f' {item[0]}="{item[1]}"',self.props.items()))

   def __repr__(self):
      return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
   
class LeafNode(HTMLNode):

     def __init__(self, tag, value, props=None):
         super().__init__(tag,value,None,props)
     
     def to_html(self):
         if self.value == None:
             raise ValueError("Leaf Node must have a value")
         if self.tag == None:
             return f"{self.value}"
         return f"<{self.tag}>{self.value}</{self.tag}>"
         