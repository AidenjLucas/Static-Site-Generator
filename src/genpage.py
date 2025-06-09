import os
from markdown_blocks import markdown_to_html_node




def generate_page(from_path, template_path, dest_path,base_path):
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
    template_html = template_html.replace(r'href="/"',f'href="{base_path}"')
    template_html = template_html.replace(r'src="/"',f'src="{base_path}"')
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
        
    with open(dest_path,"w") as f:
        f.write(template_html)
        f.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path,base_path):
    
    for file in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content,file)
        if os.path.isfile(file_path):
            des_path = os.path.join(dest_dir_path,file[:-3] +".html")
            generate_page(file_path,template_path,des_path,base_path)
        else:
            generate_pages_recursive(file_path,template_path,os.path.join(dest_dir_path,file),base_path)
    
  


def extract_markdown(markdown):
    lines =  markdown.splitlines()
    header = ""
    for line in lines:
        if "#" in line and line.count("#") == 1:
           header += line.strip("#")
           return header.strip()
        
    raise Exception("No Header")