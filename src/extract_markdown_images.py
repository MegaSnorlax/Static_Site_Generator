
import re

def extract_markdown_images(text):
    # read raw markdown text 
    # ![alt text](image_url)
    # extract alt text and url of any markdown images 
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    # return all as a list of tuples 
    # [("alt text", "iamge url"),("alt text", "image url")]
    return matches

