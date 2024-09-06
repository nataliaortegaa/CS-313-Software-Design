#  File: BST_Cipher.py
#  Student Name: Natalia Ortega
#  Student UT EID: no4432


import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:
    def __init__(self, key):
        self.root = None
        added = set()
        for char in key:
            if self.isValidCh(char) and char not in added:
                self.insert(char)
                added.add(char)

    def insert(self, ch):
        new_node = Node(ch)

        if not self.root:
            self.root = new_node
            return
        else:
            current = self.root
            parent = None
            while current:
                parent = current
                if ch < current.ch:
                    current = current.left
                else:
                    current = current.right

            if ch < parent.ch:
                parent.left = new_node
            else:
                parent.right = new_node

    def encrypt_ch(self, ch):
        path = ""
        current = self.root
        if current.ch == ch:
            return "*"
        while current and current.ch != ch:
            if ch < current.ch:
                current = current.left
                path += "<"
            else:
                current = current.right
                path += ">"
        return path

    def decrypt_code(self, code):
        current = self.root
        for char in code:
            if char == "*":
                return current.ch
            elif char == "<":
                current = current.left
            elif char == ">":
                current = current.right

            if not current:
                return ""
        return current.ch

    def encrypt(self, message):
        ret = ""
        for char in message:
            if self.isValidCh(char):
                ret += self.encrypt_ch(char) + "!"
        return ret[:-1]

    def decrypt(self, codes_string):
        ret = ""
        paths = codes_string.split("!")
        for path in paths:
            ret += self.decrypt_code(path)
        return ret

    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def isValidLetter(self, ch):
        return "a" <= ch <= "z"

    def isValidCh(self, ch):
        return ch == " " or self.isValidLetter(ch)

''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
