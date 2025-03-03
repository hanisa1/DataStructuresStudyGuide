class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if not root:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def search(self, root, key):
        if not root or root.value == key:
            return root
        return self.search(root.left, key) if key < root.value else self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

# Example Usage
bst = BST()
bst.root = bst.insert(None, 10)
bst.insert(bst.root, 5)
bst.insert(bst.root, 15)
bst.inorder(bst.root)  # Output: 5 10 15