import unittest

from splitnodeslink import split_nodes_link
from textnode import TextType, TextNode


class MyTestCase(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(expected, actual)

    def test_split_nodes_link_no_links(self):
        node = TextNode("This is text with no links", TextType.TEXT)
        actual = split_nodes_link([node])
        expected = [TextNode("This is text with no links", TextType.TEXT)]
        self.assertEqual(expected, actual)

    def test_split_nodes_link_with_trailing_text(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) too!",
            TextType.TEXT,
        )
        actual = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" too!", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
