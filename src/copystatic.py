import os
import shutil
from markdown_blocks import markdown_to_html_node

def copy_files(src,dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    else:
        shutil.rmtree(dst)
        os.mkdir(dst)
    
    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
       
        if os.path.isfile(src_path):
            shutil.copy(src_path,dst)
        else:
            os.mkdir(dst_path)
            copy_files(src_path,dst_path)

def extract_markdown(markdown):
    lines =  markdown.splitlines()
    header = ""
    for line in lines:
        if "#" in line and line.count("#") == 1:
           header += line.strip("#")
           return header.strip()
        
    raise Exception("No Header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        from_md = f.read()
        f.close()
    with open(template_path, 'r') as f:
        template_md = f.read()
        f.close()
  
    from_html = markdown_to_html_node(from_md).to_html()
    template_html = markdown_to_html_node(template_md).to_html()
    title = extract_markdown(from_md)

    template_html = template_html.replace(r"{{ Title }}", f"{title}")
    template_html = template_html.replace(r"{{ Content }}", f"{from_html}")

    with open(dest_path,"w") as f:
        f.write(template_html)
        f.close()



    # block quotes look like > "I am in fact a Hobbit in all but size." > > -- J.R.R. Tolkien
    # unordered list messed up because of italics
   