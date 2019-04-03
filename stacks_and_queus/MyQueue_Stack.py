import os

class MyQueue:

    def __init__ (self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    
    def push (self, data):
        self.s1.append (data)
    
    def pop (self):
        while s1:
            s2.append (s1.pop())
        
        x = s2.pop()
        return x
    

s1 = []
s2 = []
q = MyQueue (s1, s2)

q. push (10)
q.push (20)
q.push (30)
q.push (40)

x = q.pop ()

print (x)