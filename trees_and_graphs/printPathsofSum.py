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

def printPaths (root, sum_so_far, sum, paths):
    if root is None:
        return

    sum_so_far += root.data
    paths.append (root.data)
    if sum_so_far == sum:
        print (paths)
        
    if root.left:
        printPaths (root.left, sum_so_far, sum, paths)
    if root.right:
        printPaths (root.right, sum_so_far, sum, paths)
    #remove current element
    paths.pop(-1)

bt = BinaryTree (10)
bt.insert (5)
bt.insert (20)
bt.insert (15)
bt.insert (30)
bt.insert (25)

paths = []
printPaths (bt.root, 0, 15, paths)