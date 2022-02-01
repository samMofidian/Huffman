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


def chars_counts_2d_list(text):
    """
    receive text as string and make 2d-list of words in the text and their repetition
    :param text:
    :return: created 2d-list
    """
    # cast text to list of chars
    text_chars_list = list(text)

    # distinct elements
    set_of_chars = set(text_chars_list)

    # init 2d list
    chars_counts_list = [[""]*len(set_of_chars), [1]*len(set_of_chars)]

    # iterator
    i = 0

    # make 2d-list(top-side char | down-side count)
    for j in set_of_chars:
        chars_counts_list[0][i] = j
        chars_counts_list[1][i] = text_chars_list.count(j)
        i += 1

    return chars_counts_list


def create_nodes_list(chars_counts):
    """
    receive chars_counts and check if it's list or dictionary create proper nodes-list from it
    :param chars_counts:
    :return: nodes-list
    """
    # init nodes list
    nodes_list = []

    # chars_counts type is list
    if isinstance(chars_counts, list):
        # create chars-list
        chars_list = [i for i in chars_counts[0]]

        # create count-list
        counts_list = [i for i in chars_counts[1]]

        # add node to nodes_list (from 2d-list)
        for i in range(len(chars_list)):
            # make node for each char
            char_node = Node(data=chars_list[i], count=counts_list[i])
            nodes_list.append(char_node)

    # chars_counts type is dict
    elif isinstance(chars_counts, dict):
        # add node to nodes_list (from dictionary)
        for char in chars_counts:
            # make node for each char
            char_node = Node(data=char, count=chars_counts[char])
            nodes_list.append(char_node)

    return nodes_list


def huffman_tree(text):
    """
    create huffman tree
    :param text:
    :return: tree root
    """
    # make dictionary
    chars_dict = chars_count_dict(text)

    # make nodes list
    nodes_list = create_nodes_list(chars_dict)

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


def huffman_tree_using_list(chars_counts_list):
    """
    create huffman tree using 2d-list
    :param chars_counts_list:
    :return: tree root
    """
    # make nodes list
    nodes_list = create_nodes_list(chars_counts_list)

    # do while there is at least 2 elements in list
    while len(nodes_list) >= 2:
        # sort nodes_list by count
        # nodes_list = sorted(nodes_list, key=lambda node: node.count)
        bubble_sort(nodes_list)

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


def is_leaf(node):
    """
    check if node is leaf
    :param node:
    :return: bool
    """
    if node.left is not None or node.right is not None:
        return False
    return True


def code_generator(tree_node, stored='', counter=0, codes_dict={}):
    """
    calculate code for huffman tree leaves(single chars) recursively
    :param counter: to solve shallow copy problem in dict()
    :param tree_node:
    :param stored:
    :param codes_dict:
    :return: codes_dict
    """
    # check if it's first time this function call then empty codes_dict
    if counter == 0:
        codes_dict.clear()
    counter += 1

    # make code for each leaf(append while iterate and pass branches)
    code = stored + tree_node.code

    # add leaf code to codes_dict
    if is_leaf(tree_node):
        codes_dict[tree_node.data] = code

    # go to leaf and make leaf code
    if tree_node.left:
        code_generator(tree_node.left, code, counter=counter)
    if tree_node.right:
        code_generator(tree_node.right, code, counter=counter)

    return codes_dict


def encode(text, codes_dict):
    """
    huffman encoding
    :param codes_dict:
    :param text:
    :return:
    """
    # init result list
    res = []

    # append each code of each char in text to result list
    for i in text:
        res.append(codes_dict[i])

    # cast res to string and return
    return ''.join(res)


def decode(encoded, tree_node):
    """
    decode encoded text by huffman tree
    :param encoded:
    :param tree_node:
    :return:
    """
    # store tree root
    root = tree_node

    # init result list
    res = []

    for i in encoded:
        # if i is 0 go to left else go to right
        if i == '0':
            tree_node = tree_node.left
        else:
            tree_node = tree_node.right

        # if leaf touched then append leaf data to result list and set tree_node to root(start over)
        if is_leaf(tree_node):
            res.append(tree_node.data)
            tree_node = root

    # cast res to string and return
    return ''.join(res)


def is_efficient(text, codes_dict):
    """
    check if it's efficient to compress
    :param text:
    :param codes_dict:
    :return:
    """
    # calculate space usage of plain text
    before = len(text) * 8

    # calculate space usage after encoding
    after = 0
    for char in codes_dict:
        after += len(codes_dict[char]) * text.count(char)

    return True if after < before else False


def bubble_sort(lst):
    """
    bubble sort use in huffman_tree function to sort list based on repetition-count in dictionary
    :param lst:
    :return:
    """
    for i in range(len(lst)):
        # check if sorted or not
        has_changed = False

        for j in range(len(lst)-i-1):
            # compare count
            if lst[j].count >= lst[j+1].count:
                # swap
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

                # changed and not sorted
                has_changed = True

            # # if count were equal base on alphabetic
            # elif lst[j].count == lst[j+1].count and str(lst[j]) < str(lst[j+1]):
            #     # swap
            #     temp = lst[j]
            #     lst[j] = lst[j+1]
            #     lst[j+1] = temp
            #
            #     # changed and not sorted
            #     has_changed = True

        # hasn't  changed and sorted
        if not has_changed:
            break
