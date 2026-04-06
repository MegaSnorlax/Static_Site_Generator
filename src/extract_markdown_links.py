
import re 


def extract_markdown_links(text):
    # read raw markdown text 
    # [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)
    # extract alt text and url of any markdown images 
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    # return all as a list of tuples 
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    return matches
