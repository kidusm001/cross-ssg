from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Type is not part of the Enum")
    
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"src":text_node.url, "alt":text_node.text})
