import re

def extract_markdown_images(text):
    # pattern = r"!\[(.*?)]\((.*?)\)"
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
