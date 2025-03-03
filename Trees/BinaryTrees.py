class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

# Example Usage
bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.inorder(bt.root)  # Output: 2 1 3