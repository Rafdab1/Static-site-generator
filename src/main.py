from site_generation import generate_pages_recursive, generate

def main():
    from_path = "/home/rafdab/workspace/github.com/Rafdab1/public/content"  # path to directory with all .md files and its contents
    template_path = "/home/rafdab/workspace/github.com/Rafdab1/public/template.html" # template for the page
    dest_path = "/home/rafdab/workspace/github.com/Rafdab1/public/public" # path to directory thats going to contain all of .html files and constnets
    generate("/home/rafdab/workspace/github.com/Rafdab1/public")
    generate_pages_recursive(from_path,template_path,dest_path)
main()