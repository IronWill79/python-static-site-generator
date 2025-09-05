from htmlnode import LeafNode
from textnode import TextNode, TextNodeType


def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextNodeType.TEXT:
            return LeafNode(None, text_node.text)
        case TextNodeType.BOLD:
            return LeafNode('b', text_node.text)
        case TextNodeType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextNodeType.CODE:
            return LeafNode('code', text_node.text)
        case TextNodeType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextNodeType.IMAGE:
            return LeafNode('img', "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Invalid text node - {text_node}")
