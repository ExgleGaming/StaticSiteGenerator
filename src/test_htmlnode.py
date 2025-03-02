import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(' href="https://example.com" target="_blank"', node.props_to_html())

    def test_none_value_in_props(self):
        # Arrange
        node = HTMLNode(props={"href": None, "class": "example"})
        self.assertEqual(' class="example"', node.props_to_html()) # Act and Assert, Props with `None` values should be omitted

    def test_non_string_value_in_props(self):
        # Arrange
        node = HTMLNode(props={"data-id": 123})
        self.assertEqual(' data-id="123"', node.props_to_html()) #Act and Assert, Integer value should be converted to a string

    def test_init_empty_args(self):
        #each node is empty and testing the values for each argument
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual("HTMLNode(None, None, None, None)", f'{node}')

if __name__ == "__main__":
    unittest.main()
