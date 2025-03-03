
from extractmarkdownimages import extract_markdown_images
from textnode import TextNode, TextType


def split_node_image(node):
    nodes = []
    text = node.text
    images = extract_markdown_images(text)

    if len(images) == 0:
        return [node]

    for (alt, url) in images:
        curr, text = text.split(f"![{alt}]({url})", 1)

        if len(curr) > 0:
            nodes.append(TextNode(curr, TextType.TEXT))

        nodes.append(TextNode(alt, TextType.IMAGE, url))

    if len(text) > 0:
        nodes.append(TextNode(text, TextType.TEXT))

    return nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        new_nodes.extend(split_node_image(node))
    return new_nodes
