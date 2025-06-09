from textnode import *
from copystatic import copy_files
from genpage import *
from sys import argv

def main():

    base_path = "/"
    if len(argv) != 0:
        base_path = argv[0]
    

    copy_files("./static","./docs")
    generate_pages_recursive("./content", "template.html","./docs",base_path)
    return 0




if __name__ == "__main__":
    main()


