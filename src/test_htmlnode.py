import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_HTMLNode_HTMLNode(self):
        node1 = HTMLNode("tag", "value", nodeList, testProps)
        node2 = HTMLNode("tag", "value", nodeList, testProps)
        self.assertEqual(node1, node2)

    def test_not_eq_HTMLNode_HTMLNodeDifferentTag(self):
        node1 = HTMLNode("tag", "value", nodeList, testProps)
        node2 = HTMLNode("tag2", "value", nodeList, testProps)
        self.assertNotEqual(node1, node2)

    def test_eq_HTMLNodePropsToHTMLFunction_(self):
        node1 = HTMLNode("tag", "value", nodeList, testProps)
        output = node1.props_to_html()
        # print(output)
        expectedOutput = ' href="https://www.google.com" target="_blank" class="link"'
        self.assertEqual(output, expectedOutput)

testProps = {
    "href": "https://www.google.com",
    "target": "_blank",
    "class": "link"
}
testNode1 = HTMLNode("tagTestNode1", "value", None, testProps)
testNode2 = HTMLNode("tagTestNode2", "value", None, testProps)
testNode3 = HTMLNode("tagTestNode3", "value", None, testProps)
testNode4 = HTMLNode("tagTestNode4", "value", None, testProps)

nodeList = [testNode1, testNode2, testNode3, testNode4]

if __name__ == "__main__":
    unittest.main()

