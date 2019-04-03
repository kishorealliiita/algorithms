import os

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


def isListPalindrome (node):
    slow = node
    fast = node

    stack = []
    while fast.next:
        stack.append (slow.data)
        slow = slow.next
        fast = fast.next.next
    
    #slow is at middle, move to next.
    slow = slow.next
    while slow:
        x = stack.pop()
        #print (x)
        if x != slow.data:
            return False
        slow = slow.next
    
    return True

#test
node = Node (1)
node1 = Node (2)
node2 = Node (3)
node3 = Node (4)
node4 = Node (3)
node5 = Node (2)
node6 = Node (1)
node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print (isListPalindrome (node))

