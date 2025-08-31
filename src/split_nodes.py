from textnode import TextNode, TextNodeType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextNodeType):
    result = []
    for node in old_nodes:
        if node.text_type != TextNodeType.TEXT or delimiter not in node.text:
            result.append(node)
        strings = node.text.split(delimiter)
        if len(strings) != 3:
            raise Exception(f"Must have matching delimiters - {node.text}")
        result.append(TextNode(strings[0], TextNodeType.TEXT))
        result.append(TextNode(strings[1], text_type))
        result.append(TextNode(strings[2], TextNodeType.TEXT))
    return result
