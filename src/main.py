from textnode import *
from copystatic import copy_files,generate_page

def main():
    copy_files("./static","./public")
    generate_page("content/index.md","template.html","public/index.html")
    return 0





if __name__ == "__main__":
    main()


