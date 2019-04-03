import os

def diffOfChars (a, b):
    if len (a) == 0:
        return len (b)
    elif len (b) == 0:
        return len (a)

    n = len(a) - 1
    m = len(b) - 1

    d = dict()
    count = 0

    for c in a:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        
    for c in b:
        if c in d:
            d[c] -= 1
            count -=1
        else:
            count += 1
    
    for k,v in d.items():
        print (k,v)
        count += v

    return count


a = "pale"
b= "bakes"

print (diffOfChars(a,b))