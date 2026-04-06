import unittest

from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from text_node_to_html import text_node_to_html_node


class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_link(self):
        node = TextNode("static site generator", TextType.LINK, "https://www.boot.dev/courses/")
        html_node = text_node_to_html_node(node)
        html = html_node.to_html()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "static site generator")
        self.assertEqual(html, '<a href="https://www.boot.dev/courses/">static site generator</a>')


if __name__ == "__main__":
    unittest.main()

