block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    clear_blocks = []
    for block in blocks:
        if block == "":
            continue
        clear_blocks.append(block.strip())
    return clear_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    # heading
    if (block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### ")):
        return block_type_heading
    # code block
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    #quote
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    # unordered list
    if block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") or block.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    #ordered list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    # paragraph
    return block_type_paragraph


        