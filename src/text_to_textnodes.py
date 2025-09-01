from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextNodeType


def text_to_textnodes(text):
    starting_node = TextNode(text, TextNodeType.TEXT)
    nodes = split_nodes_delimiter([starting_node], '**', TextNodeType.BOLD)
    nodes = split_nodes_delimiter(nodes, '_', TextNodeType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '`', TextNodeType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
