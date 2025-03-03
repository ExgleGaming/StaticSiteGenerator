import re


def extract_markdown_links(text):
    # pattern = r"\[(.*?)]\((.*?)\)"
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
