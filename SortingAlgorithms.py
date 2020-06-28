def SelectionSort(a):
    n = len(a)
    for i in range(n):
        min_value = a[i]
        min_index = i
        for j in range(i+1,n):
            if min_value>a[j]:
                min_value = a[j]
                min_index = j
        a[min_index] = a[i]
        a[i] = min_value
    return a

#Dummy Function To call the quicksort function easily
def QuickSort(a):
    l = 0
    h = len(a)-1 
    quicksort(a,l,h)
    return a

#Actual Quicksort function
def quicksort(a,l,h):
    # l = lower Index
    # h = higher Index
    # pi = partition index to partition the array in 2 halves for further sorting of subarrays
    if l<h:
        pi = partition(a,l,h)
        quicksort(a,l,pi-1)
        quicksort(a,pi+1,h)
    
def partition(a,l,h):
    #Pivot = Value of Pivot Element In this case it is last element in array
    pivot = a[h]
    # i is the index to track the smaller elements
    i = l-1

    for j in range(l,h):
        if a[j]<=pivot:
            i+=1
            #Swapping the jth and ith elements of array
            a[j],a[i] = a[i],a[j]
    #Swapping the i+1th and last element of array
    a[i+1],a[h] = a[h],a[i+1]
    return i+1

def InsertionSort(a):
    n = len(a)
    for i in range(1,n):
        j=i
        while j>0:
            if a[j]<a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
            j-=1
    return a

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

def bubbleSort(l):
	for i in range(len(l)):
		for j in range(len(l)-i-1):
			if l[j]>l[j+1]:
				temp = l[j]
				l[j] = l[j+1]
				l[j+1] = temp
	print(*l,end=" ")

