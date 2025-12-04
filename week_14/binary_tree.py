#3. Cree una estructura de objetos que asemeje un Binary Tree.
#    1. Debe incluir un método para hacer `print` de toda la estructura.

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def _print_subtree(self, node):
        if node is None:
            return

        print(node.data)
        self._print_subtree(node.left)
        self._print_subtree(node.right) 

    def print_tree(self):
        self.print_subtree(self.root)
