import os

class SetOfStacks:

    def __init__ (self, k, n):
        self.n = n
        stack = [0] * n
        self.stacks = [stack] * k
        self.cur_stack = -1
        self.top = 0

    def push (self, data):
        if self.cur_stack == -1:
            self.cur_stack = 0
        
        if self.top == -1:
            self.top == 0

        if self.top == self.n-1:
            self.cur_stack = self.cur_stack + 1
            self.top = 0
        else:
            self.top = self.top + 1
        
        self.stacks[self.cur_stack][self.top] = data
        print (self.cur_stack, self.top, data)

    
    def pop(self):
        print (self.cur_stack, self.top)
        x = self.stacks[self.cur_stack][self.top]
        print (x)

        #del self.stacks[self.cur_stack][self.top]
        if self.top == 0:
            if self.cur_stack != 0 :
                self.cur_stack = self.cur_stack - 1
            self.top = self.n -1
        else:
            self.top = self.top - 1

        return x

s = SetOfStacks(5, 10)

s.push (10)
s.push (20)
s.push (30)
s.push (40)
s.push (50)
s.push (60)
s.push (70)
s.push (80)
s.push (90)
s.push (100)
s.push (110)

x = s.pop()
y = s.pop()
y = s.pop()
y = s.pop()
y = s.pop()
y = s.pop()
y = s.pop()
y = s.pop()
y = s.pop()

print (x)
print (y)

