import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_empty_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_empty_tag_and_value(self):
        with self.assertRaises(ValueError):
            LeafNode(None, None).to_html()

    def test_leaf_to_html_with_attributes(self):
        node = LeafNode("a", "Click here", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click here</a>')

if __name__ == "__main__":
    unittest.main()
