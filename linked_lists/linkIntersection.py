import os

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

def findLength (node):
    n = 0
    while node:
        n += 1
        node = node.next

    return n

def findIntersection (node1, node2):
    l1 = findLength (node1)
    l2 = findLength (node2)

    big = node1 if l1>l2 else node2
    small = node2 if big is not node2 else node1

    diff = abs (l1-l2)

    while diff:
        big = big.next

    while big and small:
        if big == small:
            return big
        big = big.next
        small = small.next
    
    return None

node = Node(10)
node1 = Node (20)
node2 = Node (30)
node3 = Node (40)
node4 = Node (50)
node5 = Node (60)
node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

n = Node (40)
n1 = Node (50)
n2 = Node (60)
n.next = n1
n1.next = n2
n2.next = node3

n_return = findIntersection (node, n)

if n_return:
    print (n_return.data)
