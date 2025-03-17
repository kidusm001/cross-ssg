import unittest
from textnode import TextNode, TextType
from node_converter import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node1, node2)
    
    def test_ieq(self):
        node1 = TextNode("This is some bold text", TextType.BOLD)
        node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node1, node2)


    def test_eq_without_url(self):
        node1 = TextNode("This is some text", TextType.TEXT)
        node2 = TextNode("This is some text", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_eq_with_none_url(self):
        node1 = TextNode("This is some text", TextType.TEXT, None)
        node2 = TextNode("This is some text", TextType.TEXT, None)
        self.assertEqual(node1, node2)

    def test_eq_with_one_none_url(self):
        node1 = TextNode("This is some text", TextType.TEXT, None)
        node2 = TextNode("This is some text", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_ieq_different_type(self):
        node1 = TextNode("This is some anchor text", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node1, node2)

    def test_ieq_different_text(self):
        node1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is some other anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node1, node2)

    def test_ieq_different_link(self):
        node1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is some other anchor text", TextType.LINK, "https://www.bootother.dev")
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")


    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "https://www.google.com")


if __name__ == "__main__":
    unittest.main()