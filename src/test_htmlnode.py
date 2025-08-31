import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_with_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode('p', None)
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child2</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_without_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, None)
            node.to_html()
    
    def test_parent_without_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode('a', None)
            node.to_html()


if __name__ == "__main__":
    unittest.main()
