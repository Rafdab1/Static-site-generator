from site_generation import generate_page

def main():
    from_path = "/home/rafdab/workspace/github.com/Rafdab1/public/content/index.md"
    template_path = "/home/rafdab/workspace/github.com/Rafdab1/public/template.html"
    dest_path = "/home/rafdab/workspace/github.com/Rafdab1/public/public/index.html"
    generate_page(from_path,template_path,dest_path)
main()