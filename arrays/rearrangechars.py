import os

def replaceSpace(s):
    if len(s) == 0:
        return ""

    print (s)
    numSpaces=0

    m = len(s) - 1
    while (m >= 0):
        if s[m] == " ":
            numSpaces += 1
        else:
            break
        m = m-1
    
    numSpaces = numSpaces/2

    n = len(s) - 1
    while (m >= 0 and n>=0):
        if s[m] != " ":
            swap (s[m], s[n])
            m = m-1
            n = n-1
        else:
            s = s[:m] + "%20" + s[m+1:]
            m = m-2
            n = n-2
            numSpaces = numSpaces-1
        
        if numSpaces == 0:
            break
        
    return s

def swap (a, b):
    temp = a
    a = b
    b = a

s = "this is Kishore    "
print (replaceSpace(s))

        

        
    




