from node import Node


def chars_count_dict(text):
    """
    receive text as string and make dictionary of words in the text and their repetition
    :param text:
    :return: created dictionary
    """
    # cast text to list of chars
    text_chars_list = list(text)

    # init dict
    chars_dict = {}

    # distinct elements
    set_of_chars = set(text_chars_list)

    # make dictionary -> |char: char_count|
    for i in set_of_chars:
        chars_dict[i] = text_chars_list.count(i)

    return chars_dict


def huffman_tree(text):
    """
    create huffman tree
    :param text:
    :return: tree root
    """
    # make dictionary
    chars_dict = chars_count_dict(text)

    # init nodes list
    nodes_list = []

    # add node to nodes_list
    for char in chars_dict:
        # make node for each char
        char_node = Node(data=char, count=chars_dict[char])
        nodes_list.append(char_node)

    # do while there is at least 2 elements in list
    while len(nodes_list) >= 2:
        # sort nodes_list by count
        nodes_list = sorted(nodes_list, key=lambda node: node.count)

        # make combined node of two smallest node
        left = nodes_list[0]
        right = nodes_list[1]
        data = str(left) + str(right)
        count = left.count + right.count
        combined = Node(data, count, left, right)

        # relate 0 for left branches and 1 for right branches(use in code)
        left.code = '0'
        right.code = '1'

        # replace combined with two nodes made it
        nodes_list.remove(nodes_list[1])
        nodes_list.remove(nodes_list[0])
        nodes_list.append(combined)

    # when loop finished there is only one element in nodes_list(tree root)
    root = nodes_list[0]

    return root
