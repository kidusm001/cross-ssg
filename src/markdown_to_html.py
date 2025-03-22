from blocknode import BlockType
from htmlnode import *
from textnode import TextNode, TextType
from block_converter import markdown_to_blocks
from block_func import block_to_block_type
from text_converter import text_to_textnodes
from node_converter import text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_node = create_node_by_blocktype(block, block_type)
        children_nodes.append(block_node)
    return ParentNode("div",children_nodes)



def create_node_by_blocktype(block, block_type):
    match(block_type):
        case BlockType.PARAGRAPH:
            return ParentNode("p", text_to_children(block.replace("\n"," ")))
        case BlockType.HEADING:
            return ParentNode(f"h{extract_heading_level(block)}",text_to_children(block.lstrip("#").lstrip()))
        case BlockType.CODE:
            return ParentNode("pre", [code_to_children(block)])
        case BlockType.QUOTE:
            return ParentNode("blockquote", text_to_children(block.replace("> ","").replace(">","").replace("\n", " ")))
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul", ul_list_to_children(block))
        case BlockType.ORDERED_LIST:
            return ParentNode("ol", ol_list_to_children(block))

def extract_heading_level(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    
    return level

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = list(map(text_node_to_html_node, text_nodes))
    if not html_nodes:
        empty_text = TextNode("", TextType.TEXT)
        html_nodes = [text_node_to_html_node(empty_text)]
    return html_nodes

def code_to_children(code):
    lines = code.split("\n")
    
    if lines[0].strip() == "```":
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    
    code_content = "\n".join(lines) + "\n"

    text_node = TextNode(code_content, TextType.TEXT)
    code_node = text_node_to_html_node(text_node)
    return ParentNode("code",[code_node])

def ul_list_to_children(text):
    lines = text.split("\n")
    ul_list = []
    for i, line in enumerate(lines):
        if line.startswith("- "):
            text = line.replace("- ", "")
            text_nodes = text_to_textnodes(text)
            html_nodes = list(filter(lambda node: node.value,(map(lambda node: text_node_to_html_node(node),text_nodes))))
            list_node = ParentNode("li", html_nodes)
            ul_list.append(list_node)
        else:
            continue
    return ul_list
            
def ol_list_to_children(text):
    lines = text.split("\n")
    ol_list = []
    for i, line in enumerate(lines):
        if line.startswith(f"{i+1}. "):
            text = line.replace(f"{i+1}. ", "")
            text_nodes = text_to_textnodes(text)
            html_nodes = list(filter(lambda node: node.value,(map(lambda node: text_node_to_html_node(node),text_nodes))))
            list_node = ParentNode("li", html_nodes)
            ol_list.append(list_node)
        else:
            continue
    return ol_list