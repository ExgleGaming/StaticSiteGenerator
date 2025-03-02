import unittest
from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_delimiters(self):
        # Test with no delimiters
        node = TextNode("Plain text with no delimiters", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Plain text with no delimiters")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_bold_delimiter(self):
        # Test with bold delimiter
        node = TextNode("Text with a **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_code_delimiter(self):
        # Test with code delimiter (backtick)
        node = TextNode("Text with a `code` block", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text with a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)

    def test_italic_delimiter(self):
        # Test with italic delimiter
        node = TextNode("Text with an _italic_ word", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text with an ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC)
        self.assertEqual(result[2].text, " word")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_non_text_node(self):
        # Test with a node that's already a different text type
        node = TextNode("Already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Already bold")
        self.assertEqual(result[0].text_type, TextType.BOLD)

    def test_missing_closing_delimiter(self):
        # Test with a missing closing delimiter
        node = TextNode("Text with an **unclosed bold", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_empty_delimited_content(self):
        # Test with empty content between delimiters
        node = TextNode("Empty **** bold", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Empty ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " bold")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_delimiters(self):
        # Test with multiple instances of the same delimiter
        node = TextNode("This has **two** bold **words**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        # Just check the length matches the actual result
        self.assertEqual(len(result), 4)

        # Then check the content of each node
        self.assertEqual(result[0].text, "This has ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "two")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " bold ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "words")
        self.assertEqual(result[3].text_type, TextType.BOLD)

    def test_multiple_nodes(self):
        # Test with multiple nodes in the input list
        node1 = TextNode("First `code`", TextType.TEXT)
        node2 = TextNode("Already italic", TextType.ITALIC)
        node3 = TextNode("Second `code`", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)

        # Check we have 5 nodes total
        self.assertEqual(len(result), 5)

        # First node should be split into text, code
        self.assertEqual(result[0].text, "First ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)

        # Third node is the unchanged italic node
        self.assertEqual(result[2].text, "Already italic")
        self.assertEqual(result[2].text_type, TextType.ITALIC)

        # Fourth and fifth nodes come from splitting the third input node
        self.assertEqual(result[3].text, "Second ")
        self.assertEqual(result[3].text_type, TextType.TEXT)

        self.assertEqual(result[4].text, "code")
        self.assertEqual(result[4].text_type, TextType.CODE)

if __name__ == "__main__":
    unittest.main()
