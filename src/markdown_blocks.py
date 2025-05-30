from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    
    if re.match(r"^#{1,6}\s\w*",markdown) != None:
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
  
    char = ""
    line_count = 0
    matched = True
    for line in markdown.splitlines():
    
        line_count += 1
        if not line.startswith(f"{line_count}. "):
            matched = False
        curr_char = line[0:2]
        if curr_char != char and char != "" and curr_char[0] != f"{line_count}":
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
   
