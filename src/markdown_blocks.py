def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    clear_blocks = []
    for block in blocks:
        if block == "":
            continue
        clear_blocks.append(block.strip())
    return clear_blocks