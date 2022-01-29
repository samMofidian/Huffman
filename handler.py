import sys
from functions import huffman_tree, huffman_tree_using_list, encode, decode, code_generator, is_efficient, chars_counts_2d_list


def start():
    """
    start program
    """
    # check user decision
    print('do you want to continue?(y/n): ', end='')
    user_respond = input()
    if user_respond == 'y':
        pass
    elif user_respond == 'n':
        sys.exit('Goodbye Friend')
    else:
        # call recursive to receive valid input(y/n)
        print('Invalid Input')
        return start()


def do_encode(text, codes_dict):
    """
    check encoding efficiency
    :param text:
    :param codes_dict:
    :return:
    """
    # if it's efficient continue
    if is_efficient(text, codes_dict):
        return

    # user decision to continue encoding with the fact that it isn't efficient
    user_respond = input("encoding is not efficient in compressing. do you still want to encode?(y/n): ")
    if user_respond == 'y':
        return
    elif user_respond == 'n':
        return run()
    else:
        # call recursive to receive valid input(y/n)
        print('Invalid Input')
        return do_encode()


def run():
    """
    factory
    :return:
    """
    # call start
    start()

    # receive text
    text = input("please input your text:\n")

    # create 2d-list
    # chars_counts_list = chars_counts_2d_list(text)

    # create tree using 2d-list
    # tree_with_list = huffman_tree_using_list(chars_counts_list)

    # create huffman tree
    tree = huffman_tree(text)

    # create code dictionary from huffman tree
    codes = code_generator(tree)
    # codes_using_tree_with_list = code_generator(tree_with_list)

    # encode
    do_encode(text, codes)
    encoded_text = encode(text, codes)
    print('encoding result:', encoded_text)

    # decode
    decoded = decode(encoded_text, tree)
    print('decoding result:', decoded)

    # call function recursively
    return run()
