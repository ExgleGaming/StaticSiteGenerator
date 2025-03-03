import textwrap
import unittest

from markdowntoblocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = textwrap.dedent("""\
            # This is a heading




            This is a paragraph of text. It has some **bold** and *italic* words inside of it.


            * This is the first list item in a list block
            * This is a list item
            * This is another list item""")
        actual = markdown_to_blocks(text)
        expected = ["# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    textwrap.dedent("""\
                    * This is the first list item in a list block
                    * This is a list item
                    * This is another list item"""),
                    ]
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()
