import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextNodeType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextNodeType.TEXT),
                TextNode("text", TextNodeType.BOLD),
                TextNode(" with an ", TextNodeType.TEXT),
                TextNode("italic", TextNodeType.ITALIC),
                TextNode(" word and a ", TextNodeType.TEXT),
                TextNode("code block", TextNodeType.CODE),
                TextNode(" and an ", TextNodeType.TEXT),
                TextNode("obi wan image", TextNodeType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextNodeType.TEXT),
                TextNode("link", TextNodeType.LINK, "https://boot.dev"),
            ],
            nodes
        )


if __name__ == "__main__":
    unittest.main()
