from htmlnode import *   
from markdown_blocks import *
from inline_markdown import *
from textnode import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    body = ParentNode("div",[],None)
   
    for block in blocks:
        body.children.append(block_to_html(block))   
       
       
 
    return body


def block_to_html(block):
    type = block_to_block_type(block)

    match type:
        case BlockType.PARAGRAPH:
            return ParentNode("p",text_to_children(remove_newlines(block)),None)
        case BlockType.CODE:
            return ParentNode("pre",[LeafNode("code",block[3:-3])],None)
        case BlockType.ORDERED_LIST:
            return ParentNode("ol",list_to_html(block,0),None)
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul",list_to_html(block,1),None)
        case BlockType.HEADING:
            h_num = get_block_heading_tag(block)
            return LeafNode(f"h{h_num}",block[h_num+1:],None)
        case BlockType.QUOTE:
            return ParentNode("blockquote",text_to_children(block),None)
        case _:
            raise ValueError("Block has an invalid type!")
    


def text_to_children(block):
    text = text_to_textnodes(block)
    nodes = [] 
    for node in text:
        nodes.append(text_node_to_html_node(node))

    return nodes
   
def remove_newlines(block):
    return ' '.join(line.strip() for line in block.splitlines())



def list_to_html(block,flag) :
    """
    flags:
    (0 : ordered)
    (1 : unordered)
    """
    prefix_cut = 3 - flag
    lines = block.split("\n")
    nodes = []
    for line in lines:
      tmp_nodes = text_to_textnodes(line)
     
      for node in tmp_nodes:
        if len(node.text) > prefix_cut:
            if node.text_type == TextType.TEXT:
                leaf = text_node_to_html_node(node)
                leaf.tag = "li"
                leaf.value = leaf.value[prefix_cut:]
                nodes.append(leaf)
            else: 
                nodes.append(ParentNode("li",[text_node_to_html_node(node)]))
                    
    return nodes

