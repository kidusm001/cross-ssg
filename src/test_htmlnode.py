import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_multiple_children(self):
        grandchild_node1 = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("b", "grandchild")
        grandchild_node3 = LeafNode("b", "grandchild")
        child_node1 = ParentNode("span", [grandchild_node1,grandchild_node2,grandchild_node3])
        child_node2 = ParentNode("span", [grandchild_node1,grandchild_node2,grandchild_node3])
        child_node3 = ParentNode("span", [grandchild_node1,grandchild_node2,grandchild_node3])
        parent_node = ParentNode("div", [child_node1,child_node2,child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<div>"
            "<span><b>grandchild</b><b>grandchild</b><b>grandchild</b></span>"
            "<span><b>grandchild</b><b>grandchild</b><b>grandchild</b></span>"
            "<span><b>grandchild</b><b>grandchild</b><b>grandchild</b></span>"
            "</div>",
        )



if __name__ == "__main__":
    unittest.main()