from textnode import TextType, TextNode
from extract_md import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue
            
        splits = old_node.text.split(delimiter)
        if len(splits) % 2 == 0:
            # If there's an uneven number of delimiters, raise an exception
            raise ValueError(f"Invalid markdown. Unmatched delimiter {delimiter}")
            
        new_nodes.append(TextNode(splits[0], TextType.TEXT))
        
        for i in range(1, len(splits), 2):
            new_nodes.append(TextNode(splits[i], text_type))
            
            if i + 1 < len(splits):
                new_nodes.append(TextNode(splits[i + 1], TextType.TEXT))
    
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
            
        remaining_text = node.text
        image_nodes = []
        
        for image_alt, image_url in images:
            markdown_image = f"![{image_alt}]({image_url})"
            parts = remaining_text.split(markdown_image, 1)
            
            if parts[0]:  
                image_nodes.append(TextNode(parts[0], TextType.TEXT))
                
            image_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            
            remaining_text = parts[1] if len(parts) > 1 else ""
        
        if remaining_text:  
            image_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
        new_nodes.extend(image_nodes)
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
            
        remaining_text = node.text
        link_nodes = []
        
        for link_text, link_url in links:
            markdown_link = f"[{link_text}]({link_url})"
            parts = remaining_text.split(markdown_link, 1)
            
            if parts[0]:  
                link_nodes.append(TextNode(parts[0], TextType.TEXT))
                
            link_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            remaining_text = parts[1] if len(parts) > 1 else ""
        
        if remaining_text:  
            link_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
        new_nodes.extend(link_nodes)
    
    return new_nodes