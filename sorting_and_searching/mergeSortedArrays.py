import os

def merge_arrays (arr1, arr2):
    result = []

    i,j = 0,0
    while (i<len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            result.append (arr1[i])
            i += 1
        else:
            result.append (arr2[j])
            j += 1

    while (i< len(arr1)):
        result.append (arr1[i])
        i += 1
    
    while (j < len (arr2)):
        result.append (arr2[j])
        j += 1

    print (result)

arr1 = [5,10,10,15,20,25]
arr2 = [1,5,7,10,20]

merge_arrays (arr1, arr2)