from textnode import TextNode,TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        if node.text.count(delimiter) % 2 == 1:
            raise Exception("Invalid Markdown Syntax")
    
        temp_list = node.text.split(delimiter)
      
        pos = 0
        for string in temp_list:
            if string == "":
                pos+=1 
                continue
            if pos % 2 == 0:
                node_list.append(TextNode(string,TextType.TEXT))
            else:
                node_list.append(TextNode(string,text_type))
            pos+=1
          
    return node_list

def split_nodes_image(old_nodes):
    node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)

        not_closed = re.search(r'!\[[^\]]*$|!\[[^\]]*\]\([^\)]*$', node.text)
        if not_closed:
            raise Exception("invalid markdown, formatted section not closed")
        
        images = extract_markdown_images(node.text)
        list = re.split(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",node.text)

        if len(images) == 0:
            node_list.append(node)
            continue
       
        i = 0
        while i < len(list) - 1:
            if list[i] == "":
                i+=1
            if list[list.index(list[i]) + 1].startswith("https://"):
                node_list.append(TextNode(list[i], TextType.IMAGE, list[i + 1]))
                i += 2
            else:
                node_list.append(TextNode(list[i], TextType.TEXT))
                i += 1
      


    return node_list

def split_nodes_link(old_nodes):
    node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
        
        not_closed = re.search(r'!\[[^\]]*$|!\[[^\]]*\]\([^\)]*$', node.text)
        if not_closed:
            raise Exception("invalid markdown, formatted section not closed")
        
        links = extract_markdown_links(node.text)
        list = re.split(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",node.text)
       
        if len(links) == 0:
            node_list.append(node)
            continue
        
        i = 0
        while i < len(list) - 1: 
            if list[i] == "":
                i+=1
            if list[list.index(list[i]) + 1].startswith("https://"):
                node_list.append(TextNode(list[i], TextType.LINK, list[i + 1]))
                i += 2
            else:
                node_list.append(TextNode(list[i], TextType.TEXT))
                i += 1

    return node_list

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
