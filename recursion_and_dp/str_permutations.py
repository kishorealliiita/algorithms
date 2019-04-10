import os

def permuatations (s):
    n = len (s)
    prefix = ''
    permHelper (prefix, s, n)


def permHelper (prefix, s, n):
    if len (prefix) == n:
        print (prefix)
    
    for i in range (0, len(s)):
        cur = s[i]
        rem = s[0:i] + s[i+1:] 
        permHelper (prefix + cur, rem , n)

permuatations ("abc")