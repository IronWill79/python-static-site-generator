import unittest

from textnode import TextNode, TextNodeType
from text_to_html import text_node_to_html_node


class TestTextToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode('This is a test node', TextNodeType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a test node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextNodeType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'This is a bold text node')

    def test_italic(self):
        node = TextNode("This is an italic text node", TextNodeType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, 'This is an italic text node')

    def test_code(self):
        node = TextNode("This is a code text node", TextNodeType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, 'This is a code text node')

    def test_link(self):
        node = TextNode("This is a link node", TextNodeType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'This is a link node')
        self.assertEqual(html_node.props_to_html(), ' href="https://www.google.com"')

    def test_image(self):
        node = TextNode("This is an image node", TextNodeType.IMAGE, "image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertIn('src="image.png"', html_node.props_to_html())
        self.assertIn('alt="This is an image node"', html_node.props_to_html())


if __name__ == "__main__":
    unittest.main()
