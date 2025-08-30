import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_works_with_no_props(self):
        node = HTMLNode('h1', 'test header', None, None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_works_for_image(self):
        node = HTMLNode('img', 'alt text', None, {'href': 'image.png', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), ' href="image.png" target="_blank"')

    def test_repr(self):
        node = HTMLNode('h1', 'test header', None, None)
        self.assertEqual(node.__repr__(), "HTMLNode(h1, test header, None, None)")

    def test_leaf_to_html_p(self):
        node = LeafNode('p', 'Hello, world!')
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode('a', 'Click me!', {'href': "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_plain(self):
        node = LeafNode(None, 'alt text')
        self.assertEqual(node.to_html(), 'alt text')


if __name__ == "__main__":
    unittest.main()
