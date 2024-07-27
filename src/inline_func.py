from textnode import (TextNode,text_type_bold,text_type_code,text_type_italic,text_type_text)
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        sub_strings = node.text.split(delimiter)
        if len(sub_strings) % 2 == 0:
            raise Exception(f"Canot find closing delimeter {node}")
        for i in range (len(sub_strings)):
            if sub_strings[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sub_strings[i], text_type_text))
            else:
                new_nodes.append(TextNode(sub_strings[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)