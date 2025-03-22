import os
import re
import shutil
from textnode import *
from markdown_to_html import markdown_to_html_node

def main():
    # Get the directory where main.py is located (src)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate one directory up to get to the project root
    base_dir = os.path.dirname(current_dir)
    
    # Construct paths relative to the project root
    static_dir = os.path.join(base_dir, "static")
    public_dir = os.path.join(base_dir, "public")
    content_dir = os.path.join(base_dir, "content")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    cp_content(static_dir, public_dir)
    # generate_page(os.path.join(content_dir, "index.md"), os.path.join(base_dir, "template.html"), os.path.join(public_dir, "index.html"))
    generate_pages_recursive(content_dir,  os.path.join(base_dir, "template.html"), public_dir)

def cp_content(source, destination):
    # For the initial call, clear the destination directory
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    
    # Get all items in the source directory
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)
        
        if os.path.isfile(source_item):
            # Copy file directly
            shutil.copy(source_item, destination_item)
            print(f"Copied file: {source_item} to {destination_item}")
        else:
            # Create subdirectory and recursively copy contents
            os.mkdir(destination_item)
            cp_content(source_item, destination_item)
            print(f"Processed directory: {source_item} to {destination_item}")

def extract_title(markdown):
    unformated_h1 = ""
    for line in markdown.split("\n"):
        if line.strip().startswith("# "):
            unformated_h1 = line
            break
    if unformated_h1 == "":
        raise Exception("No heading 1 found")
    formated_h1 = unformated_h1.replace("# ","").replace("\n", "").strip()
    return formated_h1

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        md = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()
    title = extract_title(md)
    temp_with_title = template.replace("{{ Title }}", title)
    temp_with_content = temp_with_title.replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path,"w") as file:
        file.write(temp_with_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        source_item = os.path.join(dir_path_content, item)
        dest_item = os.path.join(dest_dir_path, item)

        if os.path.isfile(source_item):
            generate_page(source_item, template_path, os.path.join(dest_dir_path, "index.html"))
        
        else:
            os.mkdir(dest_item)
            generate_pages_recursive(source_item, template_path, dest_item)




if __name__ == "__main__":
    main()
