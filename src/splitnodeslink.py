from extractmarkdownlinks import extract_markdown_links
from textnode import TextNode, TextType


def split_node_link(node):
    nodes = []
    text = node.text
    links = extract_markdown_links(text)

    if len(links) == 0:
        return [node]

    for (link, url) in links:
        curr, text = text.split(f"[{link}]({url})", 1)

        if len(curr) > 0:
            nodes.append(TextNode(curr, TextType.TEXT))

        nodes.append(TextNode(link, TextType.LINK, url))

    if len(text) > 0:
        nodes.append(TextNode(text, TextType.TEXT))

    return nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node_link(node))
    return new_nodes
