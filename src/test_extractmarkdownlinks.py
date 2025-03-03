import unittest

from extractmarkdownlinks import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "some text and some [link text](https://example.com) or [other link](https://example.com/about)"
        expected = [("link text", "https://example.com"),
                    ("other link", "https://example.com/about")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
