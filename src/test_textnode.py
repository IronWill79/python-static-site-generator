import unittest

from textnode import TextNode, TextNodeType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a text node", TextNodeType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_equal_when_text_different(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is another text node", TextNodeType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_when_type_different(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a text node", TextNodeType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_equal_when_url_different(self):
        node = TextNode("This is an image node", TextNodeType.IMAGE, "image.png")
        node2 = TextNode("This is an image node", TextNodeType.IMAGE, "image.jpg")
        self.assertNotEqual(node, node2)

    def test_not_equal_when_one_url_missing(self):
        node = TextNode("This is an image node", TextNodeType.LINK)
        node2 = TextNode("This is an image node", TextNodeType.LINK, "image.jpg")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
