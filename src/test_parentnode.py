import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq_HTMLNode_HTMLNode(self):
        parentNode1 = ParentNode("p",  [leafNode1, leafNode2], testProps)
        parentNode2 = ParentNode("p",  [leafNode1, leafNode2], testProps)

        # print(parentNode1.to_html())
        # print(parentNode2.to_html())
        
        self.assertEqual(parentNode1, parentNode2)

    def test_eq_HTMLNode_HTMLNode_toHTMLMethod(self):
        parentNode1 = ParentNode("p",  [leafNode1, leafNode2], testProps)
        parentNode2 = ParentNode("p",  [leafNode1, leafNode2], testProps)

        toHTML1 = parentNode1.to_html()
        toHTML2 = parentNode2.to_html()
        
        self.assertEqual(toHTML1, toHTML2)

    def test_eq_HTMLNode_HTMLNode_toHTMLMethod(self):
        parentNode1 = ParentNode("p",  [leafNode1, leafNode2], testProps)
        parentNode2 = ParentNode("p",  [leafNode1, leafNode2], testProps)
        parentNode3 = ParentNode("h1",  [parentNode1, leafNode2], testProps)

        toHTML1 = parentNode1.to_html()
        toHTML2 = parentNode2.to_html()
        toHTML3 = parentNode3.to_html()
        # print(f"parentNode1: {toHTML1}")
        # print(f"parentNode2: {toHTML2}")
        # print(f"parentNode3: {toHTML3}")
        
        self.assertEqual(toHTML1, toHTML2)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)


testProps = {
    "href": "https://www.google.com",
    "target": "_blank",
    "class": "link"
}

leafNode1 = LeafNode("b", "leafNode1 value", )
leafNode2 = LeafNode(None, "leafNode2 value", )
leafNode3 = LeafNode("i", "leafNode3 value",  testProps)
parentNode1 = ParentNode("p",  [leafNode1, leafNode2], testProps)
parentNode2 = ParentNode("h1",  [leafNode1, leafNode2], testProps)
parentNode3 = ParentNode("h1",  [parentNode1, leafNode2], testProps)

if __name__ == "__main__":
    unittest.main()

