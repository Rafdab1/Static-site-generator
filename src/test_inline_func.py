import unittest

from textnode import TextNode
from inline_func import *

class test_inline_functions(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        test_node = TextNode("This is text with a **bolded phrase** in the middle",text_type_text)
        self.assertEqual(split_nodes_delimiter([test_node],"**",text_type_bold),[TextNode("This is text with a ", "text") ,
                                                                                 TextNode("bolded phrase", "bold"),
                                                                                 TextNode(" in the middle", "text")])
        
    def test_split_nodes_delimiter_only_code_type(self):
        node = TextNode("`code block``Only code`", text_type_text)
        self.assertEqual(split_nodes_delimiter([node],"`",text_type_code),[ TextNode("code block", text_type_code), TextNode("Only code", text_type_code)])

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_images(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text),[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])


if __name__ == "__main__":
    unittest.main()