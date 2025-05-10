
# Chapter 6 Python Code - Binary Search Tree Insert
class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return self.Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

bst = BST()
bst.insert(bst.root, 10)
bst.insert(bst.root, 5)
bst.insert(bst.root, 15)
