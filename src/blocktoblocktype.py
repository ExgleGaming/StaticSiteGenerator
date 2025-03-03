import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown):
    # Check if the block is a heading
    if re.match(r"^#{1,6} ", markdown):
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    if all(line.startswith(">") for line in markdown.split("\n")):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in markdown.split("\n")):
        return BlockType.UNORDERED_LIST
    lines = markdown.split("\n")
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    # If no other block type matches, it's a paragraph
    return BlockType.PARAGRAPH
