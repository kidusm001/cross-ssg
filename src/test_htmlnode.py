import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode(tag="p", value="this is the content", props={"class": "text-bold", "id": "para1"})
        expected = ' class="text-bold" id="para1"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_props_to_html_empty(self):
        node = HTMLNode(tag="div", value="content")
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
    
    def test_props_to_html_special_characters(self):
        node = HTMLNode(tag="a", value="link", props={"href": "https://example.com?x=1&y=2", "title": 'He said "hello"'})
        expected = ' href="https://example.com?x=1&y=2" title="He said \"hello\""'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_separate_mutable_defaults(self):
        node1 = HTMLNode(tag="span", value="node1")
        node2 = HTMLNode(tag="span", value="node2", props={"style": "color: red;"})
        node2.props["new-prop"] = "value"
        self.assertEqual(node1.props, {})  # Ensure node1.props wasn't affected by node2
        self.assertEqual(node2.props_to_html(), ' style="color: red;" new-prop="value"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode(tag="p", value="this is the content", props={"class": "text-bold", "id": "para1"})
        self.assertEqual(node.to_html(), "<p class=\"text-bold\" id=\"para1\">this is the content</p>")

    def test_leaf_to_html_empty(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="link", props={"href": "https://example.com?x=1&y=2", "title": 'He said "hello"'})
        self.assertEqual(node.to_html(), '<a href="https://example.com?x=1&y=2" title="He said \"hello\"">link</a>')


if __name__ == "__main__":
    unittest.main()