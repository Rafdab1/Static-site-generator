import unittest

from textnode import TextNode
from inline_func import *

class test_inline_functions(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        test_node = TextNode("This is text with a **bolded phrase** in the middle",text_type_text)
        self.assertEqual(split_nodes_delimiter([test_node],"**",text_type_bold),[TextNode("This is text with a ", "text") ,
                                                                                 TextNode("bolded phrase", "bold"),
                                                                                 TextNode(" in the middle", "text")])