import re

def extract_title(markdown):
    pattern = r"(?<!\#)\# (.+)"
    match = re.search(pattern, markdown)
    if match:
        return match.group(1)
    else:
        raise Exception("Markdown must contain a H1 Heading")