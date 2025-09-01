from extract_markdown_images import extract_markdown_images
from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextNodeType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextNodeType):
    result = []
    for node in old_nodes:
        if node.text_type != TextNodeType.TEXT or delimiter not in node.text:
            result.append(node)
            continue
        strings = node.text.split(delimiter)
        if len(strings) != 3:
            raise Exception(f"Must have matching delimiters - {node.text}")
        result.append(TextNode(strings[0], TextNodeType.TEXT))
        result.append(TextNode(strings[1], text_type))
        result.append(TextNode(strings[2], TextNodeType.TEXT))
    return result

def split_nodes_image(old_nodes: list[TextNode]):
    result = []
    for node in old_nodes:
        if node.text_type != TextNodeType.TEXT:
            result.append(node)
            continue
        text = node.text
        matches = extract_markdown_images(text)
        if not matches:
            result.append(node)
            continue
        sections = []
        rest = text
        for match in matches:
            image_alt, image_link = match[0], match[1]
            sections = rest.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) > 1:
                result.append(TextNode(sections[0], TextNodeType.TEXT))
            result.append(TextNode(image_alt, TextNodeType.IMAGE, image_link))
            rest = sections[1]
        if rest:
            result.append(TextNode(rest, TextNodeType.TEXT))
    return result

def split_nodes_link(old_nodes: list[TextNode]):
    result = []
    for node in old_nodes:
        if node.text_type != TextNodeType.TEXT:
            result.append(node)
            continue
        text = node.text
        matches = extract_markdown_links(text)
        if not matches:
            result.append(node)
            continue
        sections = []
        rest = text
        for match in matches:
            link_text, link_url = match[0], match[1]
            sections = rest.split(f"[{link_text}]({link_url})", 1)
            if len(sections) > 1:
                result.append(TextNode(sections[0], TextNodeType.TEXT))
            result.append(TextNode(link_text, TextNodeType.LINK, link_url))
            rest = sections[1]
        if rest:
            result.append(TextNode(rest, TextNodeType.TEXT))
    return result
