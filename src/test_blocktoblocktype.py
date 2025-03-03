import unittest
from blocktoblocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Subheading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```\nprint('Hello')\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> A single-line quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2"), BlockType.ORDERED_LIST)
        self.assertNotEqual(block_to_block_type("1. Item 1\n3. Item 2"), BlockType.ORDERED_LIST)  # Incorrect sequence

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is just a paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("- Not really a list\nbut a paragraph!"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
