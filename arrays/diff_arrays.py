# Find the difference between arrays using recursion.


def iter (A, B, n):
    diff = 0
    for i in range (n-1, -1, -1):
        diff += abs (A[i]-B[i])
    
    return diff

def diffArrays (A, B, n):
    if len (A) != len (B):
        print ("Invalid array sizes")
        return
    
    #base case
    if n == 0:
        return abs(A[0]-B[0])
    else :
        diff = abs (A[n-1]-B[n-1])
        return diff + diffArrays(A, B, n-1)
    

A = [1,2,3,10,5]
B = [1,2,3,5,6]

x = diffArrays (A, B, 5)

y = iter (A, B, 5)

print (f'diff is {x}')

print (f'y is {y}')