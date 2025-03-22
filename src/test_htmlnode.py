import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_html import markdown_to_html_node

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
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
    # Heading 1

    ## Heading 2

    ### Heading 3
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>"
        )

    def test_unordered_list(self):
        md = """
    - Item 1
    - Item 2
    - Item 3 with **bold**
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3 with <b>bold</b></li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
    1. First item
    2. Second item with `code`
    3. Third item
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item with <code>code</code></li><li>Third item</li></ol></div>"
        )

    def test_blockquote(self):
        md = """
    > This is a blockquote
    > with multiple lines and _italic_
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote with multiple lines and <i>italic</i></blockquote></div>"
        )

if __name__ == "__main__":
    unittest.main()