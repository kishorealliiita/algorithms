import os

d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def roman_to_int (s):
    n = len(s) - 1

    if s[n] not in d:
        print ("invalid roman number.")
        return -1

    num = d[s[n]]
    n = n-1
    while n >= 0:
        if s[n] not in d:
            print (f"invalid roman letter {s[n]}")
            return -1
        if d[s[n]] < d[s[n+1]]:
            if s[n] == 'I':
                if s[n+1] not in ('V', 'X'):
                    print ("invalid roman number.")
                    return -1
                else:
                    num -= d[s[n]]
            elif s[n] == 'X':
                if s[n+1] not in ('L', 'C'):
                    print ("invalid roman number.")
                    return -1
                else:
                    num -= d[s[n]]
            elif s[n] == 'C':
                if s[n+1] not in ('D', 'M'):
                    print ("invalid roman number.")
                    return -1
                else:
                    num -= d[s[n]]
            else:
                print ("invalid roman number.")
                return -1
        else:
            num += d[s[n]]
        n = n-1
    
    return num

print (roman_to_int ("MCMXCIV"))


        
