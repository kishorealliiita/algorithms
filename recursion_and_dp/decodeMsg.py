import os

# a -> 1, b -> 2, .... z -> 26

#input: "12"
#output : number of ways: 2 ("ab", "l")

def recur_num_ways (data):
    k = len(data)
    memo = [None] * (k+1)
    return helper (data, k, memo)


def helper (data, k, memo):
    if not data:
        return 1

    if k == 0:
        return 1
    
    if memo[k] != None:
        return memo[k]

    start = len(data) - k

    if data[start] == '0':
        return 0

    result = helper (data, k-1, memo)

    x = int (data[start:start+2], 10)
    
    if k>=2 and x <= 26:
        result += helper (data, k-1, memo)

    memo[k] = result
    
    return result



data = "12"
print (recur_num_ways (data))