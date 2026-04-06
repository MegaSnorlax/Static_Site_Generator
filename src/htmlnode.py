
from textnode import TextNode

class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        else:
            return False

    def to_html(self):
        raise NotImplementedError("This function is not implemented yet")
    
    def props_to_html(self):
        if self.props == None or not self.props:
            return ""
        else:
            outputString = ""
            for key, value in self.props.items():
                text = f' {key}="{value}"'
                outputString += text

            return outputString
        
    # def __repr__(self):
    #     return f""" 
    #     HTML Node 
    #     tag: {self.tag}
    #     value: {self.value}
    #     children: {self.string_children()}
    #     props: {self.props_to_html()}
    #     """
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    # def string_children(self):
    #     print(f"string_children-children: {self.children.__sizeof__()}")
    #     if self.children == None or not self.children:
    #         return ""
    #     outputString = ""
    #     for child in self.children:
    #         childTag = child.tag if not isinstance(child, TextNode) else f"-{child.text}-"
    #         # print("1")
    #         # print(f"{childTag}")
    #         if childTag == None:
    #             outputString += f"{child.value}"
    #         else:
    #             outputString += f"<{childTag}>{child.value}</{childTag}>"
    #         # print(f"outputString: {outputString}")
    #     print("done")
    #     return outputString


                



