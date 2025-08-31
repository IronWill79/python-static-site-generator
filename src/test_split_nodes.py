import unittest

from split_nodes import split_nodes_delimiter
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


if __name__ == "__main__":
    unittest.main()
