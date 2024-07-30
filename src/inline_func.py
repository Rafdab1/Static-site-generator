from textnode import (TextNode,text_type_bold,text_type_code,text_type_italic,text_type_text,text_type_image,text_type_link)
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

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_link:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        list_of_nodes_text = []
        list_of_nodes_text.append(node.text)
        for link in links:
            #some mambo jumbo to make a list of string like this 
            # ['This is text with a link ', '[to boot dev](https://www.boot.dev)', ' and ', '[to youtube](https://www.youtube.com/@bootdotdev)', ' asjdasjdjkjasd']
            temp_list = list_of_nodes_text[-1].split(f"[{link[0]}]({link[1]})")
            temp = temp_list.pop()
            temp_list.append(f"[{link[0]}]({link[1]})")
            temp_list.append(temp)
            list_of_nodes_text.pop()
            for str in temp_list:
                if str != "":
                    list_of_nodes_text.append(str)
        if len(list_of_nodes_text) == 1 and list_of_nodes_text[0] == f"[{links[0][0]}]({links[0][1]})":
            new_nodes.append(TextNode(links[0][0],text_type_image,links[0][1]))
            continue
        for i in range(len(list_of_nodes_text)):
            if list_of_nodes_text[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(list_of_nodes_text[i],text_type_text))
            else:
                temp = extract_markdown_links(list_of_nodes_text[i])
                new_nodes.append(TextNode(temp[0][0],text_type_link,temp[0][1]))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_image:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        list_of_nodes_text = []
        list_of_nodes_text.append(node.text)
        for image in images:
            #some mambo jumbo to make a list of string like this 
            # ['This is text with a link ', '![to boot dev](https://www.boot.dev)', ' and ', '![to youtube](https://www.youtube.com/@bootdotdev)', ' asjdasjdjkjasd']
            temp_list = list_of_nodes_text[-1].split(f"![{image[0]}]({image[1]})")
            temp = temp_list.pop()
            temp_list.append(f"![{image[0]}]({image[1]})")
            temp_list.append(temp)
            list_of_nodes_text.pop()
            for str in temp_list:
                if str != "":
                    list_of_nodes_text.append(str)
        if len(list_of_nodes_text) == 1 and list_of_nodes_text[0] == f"![{images[0][0]}]({images[0][1]})":
            new_nodes.append(TextNode(images[0][0],text_type_image,images[0][1]))
            continue
        for i in range(len(list_of_nodes_text)):
            if list_of_nodes_text[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(list_of_nodes_text[i],text_type_text))
            else:
                temp = extract_markdown_images(list_of_nodes_text[i])
                new_nodes.append(TextNode(temp[0][0],text_type_image,temp[0][1]))
    return new_nodes