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
            self._insert (self.root, data)

    def _insert (self, node, data):
        if node.data < data:
            if node.left is None:
                node.left = Node (data)
            else:
                self._insert (node.left, data)
        else:
            if node.right is None:
                node.right = Node (data)
            else:
                self._insert (node.right, data)

def findLCA (root, node1, node2):
    if not root:
        return None
    
    if root.data == node1 or root.data == node2:
        return root

    left = findLCA (root.left, node1, node2)
    right = findLCA (root.right, node1, node2)

    if left and right:
        return root
    
    if left:
        return left
    
    if right:
        return right

    return None

bt = BinaryTree (10)
bt.insert (5)
bt.insert (20)
bt.insert (15)
bt.insert (30)
bt.insert (25)

print (findLCA (bt.root, 5, 15).data)