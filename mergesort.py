import numpy as np
import timeit
from timeit import Timer

# Helper function
def Mergesort(arr):
    n = len(arr)
    mergesort(arr,0,n-1)

# Partitioning happens here
def mergesort(arr,l,r):
    if l<r:
        m = (l+r)//2
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)
# Merging happens here
def merge(arr,l,m,r):
    left_arr = arr[l:m+1]
    right_arr = arr[m+1:r+1]
    n1 = len(left_arr)
    n2 = len(right_arr)

    i,j,k = 0,0,0
    
    while i<n1  and j<n2:
        if left_arr[i] <= right_arr[j]:
            arr[l+k] = left_arr[i]
            i+=1
            k+=1
        else:
            arr[l+k] = right_arr[j]
            j+=1
            k+=1
    while i<n1:
        arr[l+k] = left_arr[i]
        i+=1
        k+=1
    while j<n2:
        arr[l+k] = right_arr[j]
        j+=1
        k+=1


# Functions to test performance of mergesort
"""def driver():
    x = np.random.permutation(range(2000000))
    print(x)
    Mergesort(x)
    print(x)
"""

"""if __name__ == "__main__":
    t = Timer('driver()','from __main__ import driver')
    print("Testing time to sort 999 elements",t.timeit(number=10),"in milliseconds")
    """