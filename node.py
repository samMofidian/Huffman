class Node:
    # constructor
    def __init__(self, data, count, left=None, right=None):
        self.data = data
        self.count = count
        self.left = left
        self.right = right
        self.code = ""

    def __str__(self):
        return self.data
