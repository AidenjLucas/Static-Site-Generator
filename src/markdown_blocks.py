from enum import Enum
import re
from htmlnode import *   
from markdown_blocks import *
from inline_markdown import *
from textnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if re.match(r"^#{1,6}\s\w*", markdown) != None:
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
  
    lines = markdown.splitlines()

    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(re.match(r"^\d+\. ", line) for line in lines):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
   
   

def markdown_to_blocks(markdown):
    return list(filter(lambda block: block != "",
                        map(lambda block: block.strip(), markdown.split("\n\n"))))

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
            return ParentNode("pre",[LeafNode("code",block[4:-3])],None)
        case BlockType.ORDERED_LIST:
            return ParentNode("ol",list_to_html(block,BlockType.ORDERED_LIST),None)
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul",list_to_html(block,BlockType.UNORDERED_LIST),None)
        case BlockType.HEADING:
            h_num = get_block_heading_tag(block)
            return ParentNode(f"h{h_num}",text_to_children(block[h_num+1:]),None)
        case BlockType.QUOTE:
            return ParentNode("blockquote",quote_to_html_node(block),None)
        case _:
            raise ValueError("Block has an invalid type!")
    
def text_to_children(block):
    text = text_to_textnodes(block)
    nodes = [] 
    for node in text:
        nodes.append(text_node_to_html_node(node))
    return nodes
   
def remove_newlines(block):
    return " ".join(block.split("\n"))

def get_block_heading_tag(block):
    match = re.match(r"(^#{1,6})\s\w*", block)
    return len(match.group(1))

def list_to_html(block,block_type):
    lines = block.split("\n")
    nodes = [] 
    for line in lines:
        if block_type is BlockType.ORDERED_LIST:
            text = line[3:]
        else:
            text = line[2:]
        children = text_to_children(text)
        nodes.append(ParentNode("li",children))
    return nodes

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    return  text_to_children(content)