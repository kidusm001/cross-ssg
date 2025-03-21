
def markdown_to_blocks(markdown):
    def formated_line(block):
        lines = block.split("\n")
        stripped_lines = list(map(lambda line : line.strip(), lines))
        return "\n".join(stripped_lines)
    unformated_blocks = markdown.split("\n\n")
    formated_blocks = list(map(lambda block: block.strip(),unformated_blocks))
    formated_lines_in_blocks = list(map(formated_line, formated_blocks))
    filtered_blocks = list(filter( lambda block: block != "", formated_lines_in_blocks))
    return filtered_blocks