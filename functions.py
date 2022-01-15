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
