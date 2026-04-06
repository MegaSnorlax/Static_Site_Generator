from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered_List"
    ORDERED_LIST = "Ordered_List"

#
# takes a single block of markdown text 
# returns BLockType representing the type of block it is 
#
def block_to_block_type(block):

    # heading block regex (?<!#)\#{1,6} (.*)
    pattern = r"(?<!#)\#{1,6} (.*)"

    match = re.search(pattern, block)

    if match:
        return BlockType.HEADING

    # code block regex (?<!`)`{3}\n([\s\S]*?)`{3}(?!`)
    pattern = r"(?<!`)`{3}\n([\s\S]*?)`{3}(?!`)"

    match = re.search(pattern, block)

    if match:
        return BlockType.CODE

    # quote block regex, every line: >(.*)
    pattern = r">(.*)"
    lines = block.splitlines()
    isQuoteBlock = True
    for line in lines:
        match = re.search(pattern, line)
        if not match:
            isQuoteBlock = False
            break 
    if isQuoteBlock:
        return BlockType.QUOTE

    # unordered list block regex, every line - (.*)
    pattern = r"- (.*)"
    lines = block.splitlines()
    isQuoteBlock = True
    for line in lines:
        match = re.search(pattern, line)
        if not match:
            isQuoteBlock = False
            break 
    if isQuoteBlock:
        return BlockType.UNORDERED_LIST

    # ordered list block regex, every line, requires additional checks that numbers are in order, \d.(.*)
    lines = block.splitlines()
    isQuoteBlock = True
    n = 1
    for line in lines:
        pattern = rf"{n}.(.*)"
        match = re.search(pattern, line)
        if not match:
            isQuoteBlock = False
            break 
        n += 1
    if isQuoteBlock:
        return BlockType.ORDERED_LIST 

    # if none of the above are met, then the block is a normal paragraph
    return BlockType.PARAGRAPH