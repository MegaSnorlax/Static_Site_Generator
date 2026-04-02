
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode.tag has no value")
        if self.children == None:
            raise ValueError("ParentNode.children has no value")
        else:
            middleString = ""
            for child in self.children:
                middleString += child.to_html()
            return f"<{self.tag}>{middleString}</{self.tag}>"
        
    def __repr__(self):
        return f""" 
        HTML Node 
        tag: {self.tag}
        children: {self.string_children()}
        props: {self.props_to_html}
        """



