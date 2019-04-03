import os
import sys

class Stack:

    def __init__ (self, n=10):
        self.n = n
        self.arr = [-1] * n
        self.min = sys.maxsize
        self.top = -1

    def _min_(self):
        return self.min

    def push (self, data):
        if data < self.min:
            self.min = data
        
        if self.top == -1:
            self.top = 0
        else:
            self.top = self.top + 1
        self.arr[self.top] = data
    
    def pop (self):
        x = self.arr[self.top]
        self.arr [self.top] = -1
        self.top = self.top - 1

        return x
    

s = Stack()
s.push (10)
s.push (20)

min = s._min_()
print (min)
x = s.pop ()
print (x)


