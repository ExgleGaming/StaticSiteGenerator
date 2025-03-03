import unittest

from extractmarkdownimages import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "![alt text](https://example.com/image.png) or ![](https://example.com/alt.png)"
        expected = [("alt text", "https://example.com/image.png"),
                    ("", "https://example.com/alt.png")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)

    def test_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()
