


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
        if(self.props == None or not self.props):
            return ""
        else:
            outputString = ""
            for key, value in self.props.items():
                text = f' {key}="{value}"'
                outputString += text

            return outputString
        
    def __repr__(self):
        return f""" 
        HTML Node 
        tag: {self.tag}
        value: {self.value}
        children: {self.string_children()}
        props: {self.props_to_html}
        """
    def string_children(self):
        if self.children == None or not self.children:
            return ""
        outputString = ""
        for child in self.children:
            print("1")
            print(f"{child.tag}")
            outputString += f"{child.tag}"
        return outputString


                



