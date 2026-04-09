
from textnode import TextType, TextNode
from markdown_to_html_node import markdown_to_html_node
from generate_public_directory import generate_public_directory
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

import sys

def main():

    basepath = "/"
    print(f"len(sys.argv) {len(sys.argv)}")
    if len(sys.argv) > 1 and sys.argv[1] is not None:
        print(f"sys.argv[1]: {sys.argv[1]}")
        basepath = sys.argv[1]
    print(f"basepath: {basepath}")

    generate_public_directory("static", "docs")

    # generate_page("content/index.md", "template.html", "public/index.html")#

    # comment to generate new push

    generate_pages_recursive("content/", "template.html", "docs/", basepath)

if __name__ == "__main__":
    main()