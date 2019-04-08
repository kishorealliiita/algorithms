import os

class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__ (self, root=None):
        self.root = Node (root)

    def insert (self, data):
        if self.root.data is None:
            self.root.data = data
        else:
            self._insertBST (self.root, data)

    def _insertBST (self, node, data):
        if node is None:
            return Node (data)

        if data < node.data:
            node.left = self._insertBST (node.left, data)
        else:
            node.right = self._insertBST (node.right, data)

        return node

prev = None
def inorder (root):
    global prev
    if root is None:
        return
    inorder (root.left)
    
    if prev is not None and prev > root.data:
        print ("Not a BST")
        return
    prev = root.data
    inorder (root.right)

bt = BinaryTree (10)
bt.insert (5)
bt.insert (20)
bt.insert (15)
bt.insert (30)
bt.insert (25)

inorder (bt.root)