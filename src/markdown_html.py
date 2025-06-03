from htmlnode import *   
from markdown_blocks import *
from inline_markdown import *
from textnode import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    body = ParentNode("div",[],None)
   
    for block in blocks:
        body.children.append(block_to_html(block))   
       
       
    print(body.to_html())
    return body


def block_to_html(block):
    type = block_to_block_type(block)

    match type:
        case BlockType.PARAGRAPH:
            return ParentNode("p",text_to_children(remove_newlines(block)),None)
        case BlockType.CODE:
            return LeafNode("pre","<code>" + block[3:-3] + "</code>")
        case BlockType.ORDERED_LIST:
            return ParentNode("ol",block,[],None)
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul",block,[],None)
        case BlockType.HEADING:
            h_num = get_block_heading_tag(block)
            return LeafNode(f"h{h_num}",block[h_num+1:],None)
        case BlockType.QUOTE:
            return ParentNode("blockquote",block,None)
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

