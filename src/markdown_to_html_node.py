from block import BlockType, block_to_block_type
from htmlnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from text_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextNodeType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlnodes = []
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.PARAGRAPH:
                nodes = text_to_children(block)
                htmlnodes.append(ParentNode('p', nodes))
            case BlockType.CODE:
                htmlnodes.append(
                    ParentNode('pre',
                        [ParentNode('code',
                            [text_node_to_html_node(
                                TextNode(block.strip("```").strip(), TextNodeType.TEXT)
                            )]
                        )]
                    )
                )
            case BlockType.HEADING:
                nodes = text_to_children(block)
                htmlnodes.append(ParentNode(f"h{heading_level(block)}", nodes))
            case BlockType.QUOTE:
                nodes = text_to_children(block)
                htmlnodes.append(ParentNode("blockquote", nodes))
            case BlockType.UNORDERED_LIST:
                nodes = []
                for line in block.split("\n"):
                    nodes.append(text_to_children(line[2:]))
                htmlnodes.append(
                    ParentNode("ul", list(map(lambda node: ParentNode("li", node), nodes)))
                )
            case BlockType.ORDERED_LIST:
                nodes = []
                for line in block.split("\n"):
                    nodes.append(text_to_children(line.split(". ")[1]))
                htmlnodes.append(
                    ParentNode("ol", list(map(lambda node: ParentNode("li", node), nodes)))
                )
    return ParentNode('div', htmlnodes)


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    nodes = list(map(lambda node: text_node_to_html_node(node), textnodes))
    return nodes


def heading_level(md):
    heading, rest = md.split(' ', 1)
    return len(heading)
