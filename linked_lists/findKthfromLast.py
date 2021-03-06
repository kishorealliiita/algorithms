import os

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


def findKthFromLast (node, k):
    slow = node
    fast = node
    i = 0
    while fast and i<k:
        fast = fast.next
        i = i+1

    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow.data

node = Node (10)
node1 = Node (20)
node2 = Node (30)
node3 = Node (40)
node4 = Node (50)

node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

print (findKthFromLast(node, 4))
