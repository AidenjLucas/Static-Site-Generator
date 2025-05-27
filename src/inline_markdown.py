from textnode import TextNode,TextType


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





