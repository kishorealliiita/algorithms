import os

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

    def print (self):
        n = self
        while n:
            print (n.data)
            n = n.next


def deleteMiddle (node):
    slow = node
    temp = slow
    fast = node
    prev = None

    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    
    prev.next = slow.next

    return temp

#test
node = Node (10)
node1 = Node (20)
node2 = Node (30)
node3 = Node (40)
node4 = Node (50)

node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

n = deleteMiddle (node)
n.print()