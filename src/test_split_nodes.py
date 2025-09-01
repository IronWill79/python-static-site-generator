import unittest

from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextNodeType


class TestSplitNodes(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a **text** node", TextNodeType.TEXT)
        nodes = split_nodes_delimiter([node], '**', TextNodeType.BOLD)
        test_nodes = [
            TextNode("This is a ", TextNodeType.TEXT),
            TextNode("text", TextNodeType.BOLD),
            TextNode(" node", TextNodeType.TEXT)
        ]
        self.assertEqual(nodes, test_nodes)

    def test_italic(self):
        node = TextNode("This is an _italic_ node", TextNodeType.TEXT)
        nodes = split_nodes_delimiter([node], '_', TextNodeType.ITALIC)
        test_nodes = [
            TextNode("This is an ", TextNodeType.TEXT),
            TextNode("italic", TextNodeType.ITALIC),
            TextNode(" node", TextNodeType.TEXT)
        ]
        self.assertEqual(nodes, test_nodes)

    def test_code(self):
        node = TextNode("This is a `code` node", TextNodeType.TEXT)
        nodes = split_nodes_delimiter([node], '`', TextNodeType.CODE)
        test_nodes = [
            TextNode("This is a ", TextNodeType.TEXT),
            TextNode("code", TextNodeType.CODE),
            TextNode(" node", TextNodeType.TEXT)
        ]
        self.assertEqual(nodes, test_nodes)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextNodeType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextNodeType.TEXT),
                TextNode("image", TextNodeType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextNodeType.TEXT),
                TextNode(
                    "second image", TextNodeType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextNodeType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextNodeType.TEXT),
                TextNode("to boot dev", TextNodeType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextNodeType.TEXT),
                TextNode(
                    "to youtube", TextNodeType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes
        )


if __name__ == "__main__":
    unittest.main()
