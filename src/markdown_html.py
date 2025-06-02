from htmlnode import *   
from markdown_blocks import *
from inline_markdown import *
from textnode import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_node = HTMLNode("div",None,[],None)
    print(f"\n{blocks}")
    for block in blocks:
        html = block_to_html(block)
        print(f"\n{html}")        
       
       
    
    return 

def block_to_html(block):
    type = block_to_block_type(block)

    match type:
        case BlockType.PARAGRAPH:
            return HTMLNode("p",block,None,None)
        case BlockType.CODE:
            return HTMLNode("pre","<code>" + block + "</code>",)
        case BlockType.ORDERED_LIST:
            return HTMLNode("ol",block,[],None,None)
        case BlockType.UNORDERED_LIST:
            return HTMLNode("ul",block,[],None,None)
        case BlockType.HEADING:
            return HTMLNode(f"h{get_block_heading_tag(block)}",block,None,None)
        case BlockType.QUOTE:
            return HTMLNode("blockquote",block,None,None)
        case _:
            raise ValueError("Block has an invalid type!")
    


    