import os

def isStrRotate(s1, s2):
    s2 += s2
    if s1 not in s2:
        return False

    return True

s1 = "waterbottle"
s2 = "erbottlewat"

print (isStrRotate(s1,s2))