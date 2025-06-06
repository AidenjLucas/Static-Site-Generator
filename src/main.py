from textnode import *
from copystatic import copy_files
from genpage import *

def main():

    copy_files("./static","./public")
    generate_pages_recursive("./content", "template.html","./public")
    return 0




if __name__ == "__main__":
    main()


