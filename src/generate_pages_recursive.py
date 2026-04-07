
import os

from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # making sure destination folder exists 
    os.makedirs(dest_dir_path, exist_ok=True)

    for item in os.listdir(dir_path_content):
        sourcePath = os.path.join(dir_path_content, item)
        destinationPath = os.path.join(dest_dir_path, item)
        # check if directory 
        if os.path.isdir(sourcePath):
            # recursively copy subFolder
            generate_pages_recursive(sourcePath, template_path, destinationPath, basepath)
        # else if file
        else:
            destinationPathHTML = destinationPath.replace(".md", ".html")
            generate_page(sourcePath, template_path, destinationPathHTML, basepath)