from code.textnode import *
from code.htmlnode import *

def main():
    node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank",})
    print(node)

main()