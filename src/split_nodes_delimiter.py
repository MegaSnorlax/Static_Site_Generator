
from textnode import TextNode, TextType

from leafnode import LeafNode

from extract_markdown_links import extract_markdown_links

import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimeter, text_type):

    returnList = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            returnList.extend([node])
        else:
            # print(f"count, text, text_type, delimiter: {delimeter}")
            # print(f"node.text.count(delimeter): {node.text.count(delimeter)}")
            # print(f"node.text: {node.text}")
            # print(f"node.text_type: {node.text_type}")
            if node.text.count(delimeter) == 0:
                returnList.extend([node])
            elif (node.text.count(delimeter) % 2) != 0:
                print(f" node.text.count(delimeter) {node.text.count(delimeter)}")
                raise Exception("This is invalid Markdown syntax")
            else:
                # text contains section of code bound by delimeter
                separatedText = node.text.split(delimeter)
                separatedText = [x for x in separatedText if x != ""]

                # print(f"separatedText: {separatedText}")
                returnList = []
                for i in range(len(separatedText)):
                    delimeterIsEven = False
                    if node.text.startswith(delimeter):
                        # delimeter is every odd 
                        delimeterIsEven = True
                    if delimeterIsEven:
                        if i % 2 != 0:
                            newNode = TextNode(separatedText[i], TextType.TEXT)
                        if i % 2 == 0:
                            newNode = TextNode(separatedText[i], text_type)
                    if not delimeterIsEven:
                        if i % 2 != 0:
                            newNode = TextNode(separatedText[i], text_type)
                        if i % 2 == 0:
                            newNode = TextNode(separatedText[i], TextType.TEXT)
                    returnList.extend([newNode])
    return returnList

def split_nodes_link(old_nodes: list[TextNode]):

    returnList = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            returnList.extend([node])
        else:
            pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"

            parts = []
            last_end = 0

            for match in re.finditer(pattern, node.text):
                parts.append( TextNode(node.text[last_end:match.start()], TextType.TEXT))
                # print(f"match.group(1): {match.group(1)}")
                parts.append( TextNode(match.group(1), TextType.LINK,  match.group(2)))
                last_end = match.end()

            if node.text[last_end:] != "":
                parts.append( TextNode(node.text[last_end:], TextType.TEXT))

            returnList.extend(parts)

    return returnList

def split_nodes_image(old_nodes: list[TextNode]):

    returnList = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            returnList.extend([node])
        else:
            pattern = r"\!\[(.*?)\]\((.*?)\)"

            parts = []
            last_end = 0

            for match in re.finditer(pattern, node.text):
                parts.append( TextNode(node.text[last_end:match.start()], TextType.TEXT))
                parts.append( TextNode(match.group(1), TextType.IMAGE,  match.group(2)))
                last_end = match.end()

            if node.text[last_end:] != "":
                parts.append( TextNode(node.text[last_end:], TextType.TEXT))
            returnList.extend(parts)

        #print(f"return list: {returnList}")

    return returnList
    
def text_to_textnodes(text):
    # possible split text into single lines
    textList = [text]
    for singleLine in textList:
        textNode = TextNode(singleLine, TextType.TEXT)
    textNodeList = [textNode]
    result = split_nodes_delimiter(textNodeList, "_", TextType.ITALIC)
    # print(f"result: {result}")
    result = split_nodes_delimiter(result, "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "`", TextType.CODE)

    # print(f"overall result after code: {result}")

    result = split_nodes_image(result)
    result = split_nodes_link(result)

    # print(f"overall result: {result}")
    return result

