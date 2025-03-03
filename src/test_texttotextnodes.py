import unittest

from texttotextnodes import text_to_text_nodes
from textnode import TextNode, TextType


class Test(unittest.TestCase):
    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        actual = text_to_text_nodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(expected, actual)

    def test_text_to_text_nodes_with_plain_text(self):
        text = "This is just some basic text"
        actual = text_to_text_nodes(text)
        expected = [TextNode("This is just some basic text", TextType.TEXT)]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
