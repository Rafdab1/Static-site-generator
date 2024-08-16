from copyfiles import generate
from markdown_blocks import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            if line[1] == " ":
                return line.lstrip("#").strip()
    raise Exception("No title in the markdown file")                

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")
    markdown_file = open(from_path,"r")
    markdown = markdown_file.read()
    markdown_file.close()
    template_file = open(template_path,"r")
    template = template_file.read()
    template_file.close()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title ).replace("{{ Content }}", html_string )
    index_file = open(dest_path,"w")
    index_file.write(template)
    index_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        file_path = os.path.join(dir_path_content, file)
        if os.path.isfile(file_path) and file.endswith(".md"):
            generate_page(file_path, template_path,os.path.join(dest_dir_path,file.replace(".md",".html")))
        else:
            os.mkdir(os.path.join(dest_dir_path,file))
            generate_pages_recursive(file_path, template_path, os.path.join(dest_dir_path,file))