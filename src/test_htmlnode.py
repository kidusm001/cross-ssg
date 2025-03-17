import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()