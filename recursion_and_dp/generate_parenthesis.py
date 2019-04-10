import os 

def generateParenthesis (left, right, s, arr):
    if left == 0 and right == 0:
        arr.append (s)
    
    if left > 0:
        generateParenthesis (left-1, right+1, s + '(', arr)
    
    if right > 0:
        generateParenthesis (left, right-1, s + ')', arr)


def genPars (n):
    arr = []
    generateParenthesis (3, 0, "", arr)

    print (arr)

genPars(3)
