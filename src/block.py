from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def block_to_block_type(markdown):
    if re.fullmatch(r"^\#{1,6} [\w\d\s]+", markdown):
        return BlockType.HEADING
    elif markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    else:
        lines = markdown.split("\n")
        if all(line.startswith(">") for line in lines):
            return BlockType.QUOTE
        elif all(line.startswith("- ") for line in lines):
            return BlockType.UNORDERED_LIST
        elif all(lines[i].startswith(f"{i+1}. ") for i in range(0, len(lines))):
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
