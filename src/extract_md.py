import re

def extract_markdown_images(text):
    regex_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern, text)
    return matches


def extract_markdown_links(text):
    regex_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex_pattern, text)
    return matches