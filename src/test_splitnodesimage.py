import unittest

from splitnodesimage import split_nodes_image
from textnode import TextType, TextNode


class MyTestCase(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        actual = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(expected, actual)

    def test_split_nodes_image_no_images(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        actual = split_nodes_image([node])
        expected = [TextNode("This is text with no images", TextType.TEXT)]
        self.assertEqual(expected, actual)

    def test_split_nodes_image_with_trailing_text(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) too!",
            TextType.TEXT,
        )
        actual = split_nodes_image([node])
        expected = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" too!", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
