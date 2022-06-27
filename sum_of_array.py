# sum of  any  array

from itertools import count

def sum_array(arr):
    pointer=0
    leng=len(arr)
    for i in range(leng):
        pointer+=arr[i]
    return pointer

print(sum_array([4,5,8,7,8]))

