class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("No implementation in base class")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        list_of_props = []
        for prop in self.props:
            temp_str = f"{prop}=\"{self.props[prop]}\""
            list_of_props.append(temp_str)
        return " " + " ".join(list_of_props)
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not isinstance(self.value,str):
            raise ValueError("No <value> in LeafNode")
        if self.tag == None:
            return self.value
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node needs <tag>")
        if self.children == None:
            raise ValueError("Parent node doesnt have any children")
        return_str = ""
        for node in self.children:
            return_str += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{return_str}</{self.tag}>"