
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode.value has no value")
        elif self.tag == None:
            return self.value
        elif self.props != None:
            for key, value in self.props.items():
                return f"<{self.tag} {key}=\"{value}\">{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
    # def __repr__(self):
    #     return f""" 
    #     Leaf Node 
    #     tag: {self.tag}
    #     value: {self.value}
    #     props: {self.props_to_html()}
    #     """

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"




