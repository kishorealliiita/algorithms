import os

#time O(n), space O(n)
def addKeyToMap (a, m):
    for c in a:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1

def isPermuation( a, b):
    if len (a) != len (b):
        return False
    
    m1 = dict()
    m2 = dict()

    addKeyToMap (a, m1)
    addKeyToMap (b, m2)

    for k,v in m1.items():
        if k not in m2:
            print (f"key {k} not found in m2")
            return False
        if v != m2[k]:
            print (f"unmatched {k}")
            return False
        else:
            m2.pop (k,None)

    if len (m2.keys()) != 0:
        print ("not a palindrome.")
        return False
    
    return True

a = "abdc"
b = "abcd"

print (isPermuation(a,b))

a = "xyza"
b = "abcd"

print (isPermuation(a,b))

#Time: O(nlogn)
def sortPermuation(a, b):
    a = sorted(a)
    b = sorted (b)

    if a!= b:
        return False
    
    return True

a = "bcad"
b = "abcd"

print (sortPermuation(a,b))

    
