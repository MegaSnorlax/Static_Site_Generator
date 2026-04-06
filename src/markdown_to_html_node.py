
from markdown_to_blocks import markdown_to_blocks
from blocks import BlockType, block_to_block_type
from htmlnode import HTMLNode
from split_nodes_delimiter import text_to_textnodes
from text_node_to_html import text_node_to_html_node
from parentnode import ParentNode
import re
from leafnode import LeafNode
from textnode import TextNode, TextType

#
# takes a full markdown document
# converts into a single HTMLNode
# the single HTMLNode should contain many children representing the nested elements
#
def markdown_to_html_node(markdown):

    # split the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    # print(f"blocks: {blocks}")

    childrenNodes = []

    # loop over each block
    # determine what type of block you have
    # create an HTMLNode based on the type of block
    # assign the proper child objects to the block node 
    # text_to_children(text) function - works for all block types, takes string of text,
    # returns list of HTMLNodes representing the inline markdown using previously created functions
    # code block is an exception and should be treated separately
    for block in blocks:
        blockType = block_to_block_type(block)
        if blockType == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            childNodes = text_to_children(block)
            blockNode = ParentNode("p", childNodes)
            childrenNodes.append(blockNode)
        if blockType == BlockType.HEADING:
            pattern = r"(#+)\s*(.*)"
            match = re.match(pattern, block)
            headerNum = match.group(1).count("#")
            childNodes = text_to_children(match.group(2))
            blockNode = ParentNode(f"h{headerNum}", childNodes)
            childrenNodes.append(blockNode)
        if blockType == BlockType.QUOTE:
            lines = block.splitlines()
            pattern = r">\s?(.*)"
            childNodes = []
            if len(lines) == 1:
                # print(f"lines: {lines}")
                match = re.match(pattern, lines[0])
                quoteText = (f"{match.group(1)}")
                childNodes.extend(text_to_children(quoteText))
            # else:
            #     childNodesPara = []
            #     for line in lines:
            #         match = re.match(pattern, line)
            #         quoteText = (f"{match.group(1)}")
            #         childNodesPara.extend(text_to_children(quoteText))
            #     paragraphParentNode = ParentNode("p", childNodesPara)
            #     childNodes.append(paragraphParentNode)
            # blockNode = ParentNode("blockquote", childNodes)            
            else:
                # childNodesPara = []
                for line in lines:
                    match = re.match(pattern, line)
                    quoteText = (f"{match.group(1)}")
                    childNodes.extend(text_to_children(quoteText))
                #paragraphParentNode = ParentNode("p", childNodesPara)
                #childNodes.append(childNodesPara)
            blockNode = ParentNode("blockquote", childNodes)
            childrenNodes.append(blockNode)
        if blockType == BlockType.UNORDERED_LIST:
            lines = block.splitlines()
            childNodes = []
            for line in lines:
                childNodesLine = []
                pattern = "- (.*)"
                match = re.match(pattern, line)
                childNodesLine = text_to_children(match.group(1))
                blockNode = ParentNode("li", childNodesLine)
                childNodes.append(blockNode)

            ulNode = ParentNode("ul", childNodes)
            childrenNodes.append(ulNode)
        if blockType == BlockType.ORDERED_LIST:
            lines = block.splitlines()
            childNodes = []
            for line in lines:
                childNodesLine = []
                pattern = "\d*. (.*)"
                match = re.match(pattern, line)
                childNodesLine = text_to_children(match.group(1))
                blockNode = ParentNode("li", childNodesLine)
                childNodes.append(blockNode)

            ulNode = ParentNode("ol", childNodes)
            childrenNodes.append(ulNode)
        if blockType == BlockType.CODE:
            pattern = r"(?<!`)`{3}\n([\s\S]*?)`{3}(?!`)"
            match = re.match(pattern, block)
            codeText = match.group(1)
            codeTextNode = LeafNode("code", codeText)
            preParentNode = ParentNode("pre", [codeTextNode])
            childrenNodes.append(preParentNode)





    parentHTMLNode = ParentNode("div", childrenNodes)

    return parentHTMLNode

    # make all the block nodes children under a single parent HTMLNode that is a div, and return it 



def text_to_children(block):
    splitNodes = text_to_textnodes(block)
    htmlNodes = []
    for textNode in splitNodes:
        htmlNodes.append(text_node_to_html_node(textNode))
    return htmlNodes