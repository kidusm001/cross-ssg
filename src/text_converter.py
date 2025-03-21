from split_nodes_delimiter import *

def text_to_textnodes(text: str):
    text_node = TextNode(text, TextType.TEXT)
    with_bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    with_italic = split_nodes_delimiter(with_bold, "_", TextType.ITALIC)
    with_code = split_nodes_delimiter(with_italic, "`", TextType.CODE)
    with_links = split_nodes_link(with_code)
    with_images = split_nodes_image(with_links)
    return with_images