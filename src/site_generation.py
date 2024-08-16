from copyfiles import generate
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            if line[1] == " ":
                return line.lstrip("#").strip()
    raise Exception("No title in the markdown file")                

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    generate("/home/rafdab/workspace/github.com/Rafdab1/public")
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