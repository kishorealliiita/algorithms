import os

def isPermPalindrome (s):

    if len (s) == 0:
        return True
    
    m = dict()

    for c in s:
        if c not in m:
            m[c] = 1
        else:
            del m[c]
        
    n = len (m.keys())

    print (f"n is {n}")

    for k,v in m.items():
        print (k,v)

    if n%2 == 0:
        return True
    
    return False


s = "tact coa"

print (isPermPalindrome(s))