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
  
    char = ""
    line_count = 0
    matched = True
    lines = markdown.splitlines()
    for line in lines:
        line_count += 1
        curr_char = line[0:2]

        if not line.startswith(f"{line_count}. "):
           matched = False
        if curr_char != char and char != "" and not matched:
           break

        char = curr_char
        
    if line_count == len(markdown.splitlines()):
        if char[0] == ">": return BlockType.QUOTE
        if char == "- ": return BlockType.UNORDERED_LIST
        if matched: return BlockType.ORDERED_LIST
   
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
            return ParentNode("ol",list_to_html(remove_prefix(block,BlockType.ORDERED_LIST)),None)
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul",list_to_html(remove_prefix(block,BlockType.UNORDERED_LIST)),None)
        case BlockType.HEADING:
            h_num = get_block_heading_tag(block)
            return LeafNode(f"h{h_num}",block[h_num+1:],None)
        case BlockType.QUOTE:
            return ParentNode("blockquote",text_to_children(remove_prefix(block,BlockType.QUOTE)),None)
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

def get_block_heading_tag(block):
    match = re.match(r"(^#{1,6})\s\w*", block)
    return len(match.group(1))

def list_to_html(block):
    lines = block.splitlines()
    nodes = [] 

    for line in lines:
      if len(line) > 1:
        tmp_nodes = text_to_textnodes(line)
        return_node = ParentNode("li",[])
        for node in tmp_nodes:
            return_node.children.append(text_node_to_html_node(node))     
      nodes.append(return_node)
    
    return nodes

def remove_prefix(block,block_type):
    prefix_cut = 0
    
    if block_type == BlockType.ORDERED_LIST:
        prefix_cut = 3
    if block_type == BlockType.QUOTE or block_type == BlockType.UNORDERED_LIST:
        prefix_cut = 2

    lines = block.split("\n")
    new_block = ""
    for line in lines:
        if block_type == BlockType.QUOTE:
            new_block += line[prefix_cut:] + " "
        else:    
            new_block += line[prefix_cut:] + "\n"

    return new_block.strip()