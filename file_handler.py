from functions import *


class FileHandler:

    def compress(self, filename):
        """
        receive file-name, compress the txt file content and create txt file named compressed-{filename}
        :param filename:
        :return:
        """
        with open(f'./files/{filename}.txt', 'r') as f1:
            plain_content = f1.read()
            encoded = self.__encode(plain_content)
            with open(f'./files/compressed-{filename}.txt', 'w') as f2:
                f2.write(encoded)

    @staticmethod
    def __encode(text):
        """
        encoding file content -- use in compress func
        :param text:
        :return:
        """
        # make dictionary of chars and their repetition-count
        chars_dict = chars_count_dict(text)

        # create huffman tree
        tree = huffman_tree(chars_dict)

        # create code dictionary from huffman tree
        codes = code_generator(tree)

        # return encoded text
        return encode(text, codes)

    @staticmethod
    def __decode(text, chars_dict):
        """
        encoding file content -- use in decompress func
        :param text:
        :param chars_dict:
        :return:
        """
        # create tree from chars_dict
        tree = huffman_tree(chars_dict)

        # return decoded text
        return decode(text, tree)
