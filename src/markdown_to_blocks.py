def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        if block:
            result.append(block.strip('\n'))
    return result
