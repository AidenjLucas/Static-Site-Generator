def markdown_to_blocks(markdown):
    blocks = list(filter(lambda block: block != "",
                        map(lambda block: block.strip(), markdown.split("\n\n"))))
   
    for i in range(len(blocks)):
            tmp =  blocks[i].partition("\n")
            blocks[i] = tmp[0] + tmp[1] + tmp[2].strip()
    
    return blocks
