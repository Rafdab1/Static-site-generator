text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

from htmlnode import LeafNode

class TextNode:
    def __init__(self,text, text_type, url = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url= url
    
    def __eq__(self, value: object) -> bool:
        if self.text != value.text:
            return False
        if self.text_type != value.text_type:
            return False
        if self.url != value.url:
            return False
        return True
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    posible_text_type = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in posible_text_type:
        raise Exception(f"Invalid text type: {text_node.text_type}")
    
    if text_node.text_type == text_type_text:
        return LeafNode(None,text_node.text)
    
    if text_node.text_type == text_type_bold:
        return LeafNode("b",text_node.text)
    
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == text_type_link:
        return LeafNode("a",text_node.text,{"href": text_node.url})

    if text_node.text_type == text_type_image:
        return LeafNode("img","",{"src": text_node.url, "alt": text_node.text})
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_TextNodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            list_of_TextNodes.append(node)
        words_from_node = node.value.split()
        node_text = []
        for word in words_from_node:
            if word.find(delimiter) == -1:
                node_text.append(word)
            