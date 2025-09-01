import unittest

from block import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_1(self):
        md = "# Heading 1"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_2(self):
        md = "## Heading 2"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_3(self):
        md = "### Heading 3"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_4(self):
        md = "#### Heading 4"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_5(self):
        md = "##### Heading 5"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_6(self):
        md = "###### Heading 6"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_7_fails(self):
        md = "####### Broken Heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading_without_space_fails(self):
        md = "#Broken Heading"
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_code_block(self):
        md = """```
This should be a code block
```"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote_block(self):
        md = """> This should be a quote block
>
> Still a valid quote block"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_invalid_quote_block_fails(self):
        md = """> This should be a quote block

> Still a valid quote block"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        md = """- This is part of a list
- Still part of a list"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_invalid_unordered_list_fails(self):
        md = """- This is part of a list
 Still part of a list"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list(self):
        md = """1. First item
2. Second item
3. Third item"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_invalid_ordered_list_fails(self):
        md = """1. First item
3. Second item
4. Third item"""
        block_type = block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


if __name__ == '__main__':
    unittest.main()
