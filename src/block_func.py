import re
from blocknode import BlockType

def block_to_block_type(block):
    lines = block.split("\n")
    if re.match(r"^#{1,6}", block):
        return BlockType.HEADING
    if re.match(r"^```.*```$", block, re.DOTALL):
        return BlockType.CODE
    if lines and all(map(lambda line: line.startswith(">"), lines)):
        return BlockType.QUOTE
    if lines and all(map(lambda line: line.startswith("- "), lines)):
        return BlockType.UNORDERED_LIST
    if lines and all(map(lambda line: line.startswith("- "), lines)):
        return BlockType.UNORDERED_LIST
    if len(lines) > 0 and all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    