import os

class Animal (object):
    pass

class Dog (Animal):
    def __init__ (self, data):
        print ("this is a dog.")
        self.data = data

class Cat (Animal):
    def __init__(self,data):
        print ("this is a cat.")
        self.data = data


class MyQueue:

    def __init__(self):
        self.contents = []


    def enqueue (self, data):
        self.contents.append (data)
    
    def dequeueAny (self):
        x = None
        if len(self.contents) > 0:
           x = self.contents.pop(0)

        return x

    def dequeueDog (self):
        x = None
        for i in range (0, len(self.contents)):
            if isinstance (self.contents[i], Dog):
                x = self.contents[i]
                self.contents = self.contents[0:i] + self.contents [i+1:]
                return x
        
        return x

    def dequeuCat (self):
        x = None
        for i in range (0, len(self.contents)):
            if isinstance (self.contents[i], Cat):
                x = self.contents[i]
                self.contents = self.contents[0:i] + self.contents[i+1:]
                return x

        
        return x


q = MyQueue()
q.enqueue (Dog(10))
q.enqueue (Cat (20))
q.enqueue (Dog (30))
q.enqueue (Dog(40))
q.enqueue (Cat(50))


x = q.dequeueAny ()
print (x.data)

y = q.dequeueDog()
print (y.data)

z = q.dequeuCat()
print (z.data)


d = q.dequeueDog()
print (d.data)