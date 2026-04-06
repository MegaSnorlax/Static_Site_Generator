

import os
import shutil

def generate_public_directory(sourcePath: str):

    destinationPath = "public"
    if not os.path.exists(destinationPath):
        raise Exception(f"destination path {destinationPath} does not exist")
    if not os.path.exists(sourcePath):
        raise Exception(f"source path {sourcePath} does not exist")

    # delete everything already in the public folder 

    for filename in os.listdir(destinationPath):
        filePath = os.path.join(destinationPath, filename)

        if os.path.isfile(filePath) or os.path.islink(filePath):
            print(f"unlinking: {filePath}")
            os.unlink(filePath)
        elif os.path.isdir(filePath):
            print(f"removing tree of: {filePath}")
            shutil.rmtree(filePath)
    
    # copy all files from sourcePath 

    copy_dir(sourcePath, destinationPath)

def copy_dir(source: str, destination: str):
    # making sure destination folder exists 
    os.makedirs(destination, exist_ok=True)

    for item in os.listdir(source):
        sourcePath = os.path.join(source, item)
        destinationPath = os.path.join(destination, item)
        # check if directory 
        if os.path.isdir(sourcePath):
            # recursively copy subFolder
            copy_dir(sourcePath, destinationPath)
        # else if file
        else:
            print(f"copying file: {sourcePath} to {destinationPath}")
            os.makedirs(os.path.dirname(destinationPath), exist_ok=True)
            shutil.copy2(sourcePath, destinationPath)