from textnode import *
from htmlnode import *
from inline_func import *
from markdown_blocks import *

def main():
    markdown_text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    print(markdown_to_html_node(markdown_text))
main()