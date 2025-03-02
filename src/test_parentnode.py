import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_missing_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "child")]).to_html()

    def test_missing_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_multiple_children(self):
        parent = ParentNode("div", [
            LeafNode("span", "child1"),
            LeafNode("span", "child2")
        ])
        self.assertEqual(
            parent.to_html(),
            "<div><span>child1</span><span>child2</span></div>"
        )

    def test_complex_nesting(self):
        # Create a deeply nested structure with multiple children at different levels
        leaf1 = LeafNode("b", "bold text")
        leaf2 = LeafNode("i", "italic text")
        leaf3 = LeafNode(None, "plain text")

        inner_parent1 = ParentNode("p", [leaf1, leaf2])
        inner_parent2 = ParentNode("div", [leaf3, inner_parent1])

        outer_parent = ParentNode("section", [
            LeafNode("h1", "Title"),
            inner_parent2,
            LeafNode("footer", "Footer")
        ])

        expected = "<section><h1>Title</h1><div>plain text<p><b>bold text</b><i>italic text</i></p></div><footer>Footer</footer></section>"
        self.assertEqual(outer_parent.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
