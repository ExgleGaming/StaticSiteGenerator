from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        # Skip non-TEXT nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # Process TEXT nodes
        text = old_node.text
        remaining_text = text
        result = []

        while True:
            # Find the opening delimiter
            opener_index = remaining_text.find(delimiter)
            if opener_index == -1:
                # No more delimiters, add the remaining text
                if remaining_text:
                    result.append(TextNode(remaining_text, TextType.TEXT))
                break

            # Add text before the delimiter if there is any
            if opener_index > 0:
                result.append(TextNode(remaining_text[:opener_index], TextType.TEXT))

            # Find the closing delimiter
            remaining_text = remaining_text[opener_index + len(delimiter):]
            closer_index = remaining_text.find(delimiter)

            if closer_index == -1:
                # No closing delimiter found
                raise ValueError(f"No closing delimiter '{delimiter}' found")

            # Add the delimited content with the special text type
            delimited_content = remaining_text[:closer_index]
            result.append(TextNode(delimited_content, text_type))

            # Continue with the rest of the text
            remaining_text = remaining_text[closer_index + len(delimiter):]

        new_nodes.extend(result)

    return new_nodes
