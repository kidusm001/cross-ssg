import unittest
from textnode import TextNode, TextType

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
        node1 = TextNode("This is some text", TextType.NORMAL)
        node2 = TextNode("This is some text", TextType.NORMAL)
        self.assertEqual(node1, node2)

    def test_eq_with_none_url(self):
        node1 = TextNode("This is some text", TextType.NORMAL, None)
        node2 = TextNode("This is some text", TextType.NORMAL, None)
        self.assertEqual(node1, node2)

    def test_eq_with_one_none_url(self):
        node1 = TextNode("This is some text", TextType.NORMAL, None)
        node2 = TextNode("This is some text", TextType.NORMAL)
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

if __name__ == "__main__":
    unittest.main()