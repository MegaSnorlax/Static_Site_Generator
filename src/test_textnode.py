import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_TextNodeWithoutURL_TextNodeWithoutURL(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_TextNodeWithURL_TextNodeWithURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "url.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "url.com")
        self.assertEqual(node, node2)

    def test_not_eq_TextNodeWithoutURL_TextNodeWithURL(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "url.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_TextNodeWithURL_TextNodeWithDifferentURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "url.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "url2.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_TextNodeWithURLBoldTextType_TextNodeWithtURLItalicTextType(self):
        node = TextNode("This is a text node", TextType.BOLD, "url.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "url.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_TextNodeWithURLBoldTextTypeText_TextNodeWithtURLBoldTextTypeDifferentText(self):
        node = TextNode("This is a text node", TextType.BOLD, "url.com")
        node2 = TextNode("This is a different text node", TextType.BOLD, "url.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()