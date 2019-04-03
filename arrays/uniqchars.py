import os

def isUniqueStr (s):
    l = len (s)

    if l==0 or l==1:
        return True

    m = dict()

    for i in range (0,l):
        if s[i] in m:
            m[s[i]] += 1
        else:
            m[s[i]] = 1
    
    for k,v in m.items():
        if v >1:
            print (f"duplicate {k}")
            return False
    
    return True

s = "Abcd"
d = "aabbccd"
print (isUniqueStr (s))
print (isUniqueStr (d))