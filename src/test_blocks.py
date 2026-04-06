import unittest

from blocks import BlockType, block_to_block_type


class TestTextNodeToHTML(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "### Heading"

        result = block_to_block_type(block)

        self.assertEqual(BlockType.HEADING, result)

    def test_block_to_block_type_code(self):
        block = """```
        multiline code block
        ```"""

        result = block_to_block_type(block)

        self.assertEqual(BlockType.CODE, result)

    def test_block_to_block_type_quote(self):
        block = """> quote
        > quote
        >quote
        > quote"""

        result = block_to_block_type(block)

        self.assertEqual(BlockType.QUOTE, result)

    def test_block_to_block_type_unordered_list(self):
        block = """- quote
        - quote
        - quote
        - quote"""

        result = block_to_block_type(block)

        self.assertEqual(BlockType.UNORDERED_LIST, result)

    def test_block_to_block_type_ordered_list(self):
        block = """1. quote
        2. quote
        3. quote
        4. quote"""

        result = block_to_block_type(block)

        self.assertEqual(BlockType.ORDERED_LIST, result)

    def test_block_to_block_type_invalid_ordered_list(self):
        block = """1. quote
        2. quote
        5. quote
        4. quote"""

        result = block_to_block_type(block)

        self.assertEqual(BlockType.PARAGRAPH, result)

    def test_block_to_block_type_paragraph(self):
        block = """this is 
        a paragraph
        it is only a collection 
        of lines with no double 
        space between them"""
        
        result = block_to_block_type(block)

        self.assertEqual(BlockType.PARAGRAPH, result)



if __name__ == "__main__":
    unittest.main()

