import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("this is a different text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test__repr(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(f"{node}", "TextNode(This is a link node, link, https://www.boot.dev)")

    def test_init(self):
        node = TextNode("Code node", TextType.CODE)
        self.assertEqual("Code node", node.text)
        self.assertEqual(TextType.CODE, node.text_type)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()
