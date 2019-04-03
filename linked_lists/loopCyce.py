import os

class Node:
    def __init__ (self, data):
        self.data = data
        self.Next = None
    

def startOfCycle (node):
    slow = node
    fast = node

    while (slow and fast and fast.Next):
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast:
            break
        #print (slow.data, fast.data)
    
    #print (slow.data)
    if slow != fast:
        print ("no loop")
        return None
    
    #start slow from start.
    slow = node
    while slow != fast:
        slow = slow.Next
        fast = fast.Next
        #print (slow.data)
    
    return slow

node = Node (10)
node1 = Node (20)
node2 = Node (30)
node3 = Node (40)
node4 = Node (50)
node5 = Node (60)

node.Next = node1
node1.Next = node2
node2.Next = node3
node3.Next = node4
node4.Next = node5
node5.Next = node2

n = startOfCycle (node)

if n:
    print (n.data)

    

