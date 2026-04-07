
from textnode import TextType, TextNode
from markdown_to_html_node import markdown_to_html_node
from generate_public_directory import generate_public_directory
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

import sys

def main():

    basepath = "/"
    if sys.argv[0]:
        basepath = sys.argv[0]

    generate_public_directory("static")

    # generate_page("content/index.md", "template.html", "public/index.html")#

    generate_pages_recursive("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    main()