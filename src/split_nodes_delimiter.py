from textnode import TextType, TextNode
from extract_md import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception(f"Unmatched delimiter {delimiter}")
        split_nodes = []
        for idx, text in enumerate(split_text):
            if idx % 2 == 0:
                split_nodes.append(TextNode(text, TextType.TEXT))
            else:
                split_nodes.append(TextNode(text, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        remaining_text = node.text
        image_nodes = []
        for image_alt, image_url in images:
            before, remaining_text = remaining_text.split(f"![{image_alt}]({image_url})", 1)
            image_nodes.append(TextNode(before,TextType.TEXT))
            image_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
        if not image_nodes:
            new_nodes.append(node)
        else:
            new_nodes.extend(image_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        remaining_text = node.text
        link_nodes = []
        for link_text, link_url in links:
            before, remaining_text = remaining_text.split(f"[{link_text}]({link_url})", 1)
            link_nodes.append(TextNode(before,TextType.TEXT))
            link_nodes.append(TextNode(link_text, TextType.LINK, link_url))
        if not link_nodes:
            new_nodes.append(node)
        else:
            new_nodes.extend(link_nodes)
    return new_nodes
