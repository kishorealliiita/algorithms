import os

def stringConcat (s):
    if len(s) == 0:
        return s

    count = 1
    ret = s[0]

    for i in range (1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            ret += str(count)
            ret += s[i]
            count = 1
    
    ret += str(count)
    if len(ret) > len (s):
        return s
    
    return ret

s = "aabbbcccccaaa"

print (stringConcat(s))
