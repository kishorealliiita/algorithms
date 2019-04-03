import os

class Node:
    def __init__ (self, data, next=None):
        self.data = data
        self.next = next

    def print (self):
        cur = self
        while cur:
            print (cur.data)
            cur = cur.next
    
def partitionList (node, x):

    small = []
    big = []

    while node:
        #print (node.data)
        if node.data < x:
            small.append(node.data)
        else:
            big.append (node.data)
        node = node.next
    
    n = None
    prev = n
    for i in range (0, len(small)):
        if n:
            next = Node (small[i])
            n.next = next
            n = n.next
        else:
            n = Node (small[i])
            prev = n

    
    for i in range (0, len(big)):
        if n:
            next = Node (big[i])
            n.next = next
            n = n.next
        else:
            n = Node (big[i])
            prev = n
    
    return prev

#test
node = Node (3)
node1  = Node (5)
node2 = Node (1)
node3 = Node (10)
node4 = Node (4)

node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

#node.print()
n = partitionList (node, 5)
n.print()






