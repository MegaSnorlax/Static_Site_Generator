
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os 

def generate_page(from_path, template_path, dest_path, basepath):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as fromFile:
        fromContent = fromFile.read()
    with open(template_path, "r") as templateFile:
        templateContent = templateFile.read()

    singleHTMLNode = markdown_to_html_node(fromContent)

    title = extract_title(fromContent)

    with open(template_path, "r", encoding="utf-8") as templateFile:
        html = templateFile.read()

    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", singleHTMLNode.to_html())
    html = html.replace('href="/', f'href="{basepath}/')
    html = html.replace('src="/', f'src="{basepath}/')

    # check if dest path exist 

    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    