import os

class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None

    def print (self):
        n = self
        while (n):
            print (n.data)
            n = n.next


def removeDuplicates (node):
    if not node:
        return node
    
    head = node
    temp = head
    prev = None
    d = dict ()
    while (head):
        if head.data in d:
            #print (head.data)
            prev.next = head.next
        else:
            d[head.data] = True
    
        prev = head
        head = head.next
    
    return temp

#test
node = Node(10)
node1 = Node (11)
node2 = Node (11)
node3 = Node (15)
node4 = Node (16)
node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

n = removeDuplicates (node)
n.print()
