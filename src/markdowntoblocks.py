def markdown_to_blocks(markdown):
    """
    * Break the markdown string based on double newline characters
    * Strip leading and trailing whitespace from each entry
    * Remove any empty entries
    :param markdown:  The text to be converted
    :return: List of block-level content
    """
    return list(filter(lambda block: len(block) > 0, map(lambda block: block.strip(), markdown.split('\n\n'))))
