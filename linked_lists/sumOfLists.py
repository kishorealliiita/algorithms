import os

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

    def print (self):
        cur = self
        while cur:
            print (cur.data)
            cur = cur.next

def list_size (l):
    n = 0
    cur = l
    while cur:
        n += 1
        cur = cur.next
    return n

def sumOfLists (l1, l2):

    l3 = None
    prev = l3
    
    rem = 0
    while l1 and l2:
        x = (l1.data + l2.data + rem)
        sum = x %10
        rem = int (x/10)
        if l3:
            y = Node (sum)
            l3.next = y
            l3 = l3.next
        else:
            l3 = Node (sum)
            prev = l3
        l1 = l1.next
        l2 = l2.next
    
    if l1:
        sum = (l1.data) % 10 + rem
        rem = sum/10
        y = Node (sum)
        l3.next = y
    
    elif l2:
        sum = (l2.data) % 10 + rem
        rem = sum/10
        y = Node (sum)
        l3.next = y

    if rem != 0:
        y = Node (rem)
        l3.next = y

    return prev

l1 = Node (7)
node1 = Node (1)
node2 = Node (6)
l1.next = node1
node1.next = node2

l2 = Node (5)
n1 = Node (9)
n2 = Node (2)
l2.next = n1
n1.next = n2

n = sumOfLists (l1,l2)
n.print ()

           


