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

#Driver Function
"""if __name__ == "__main__":
    n = int(input())
    a=[]
    for _ in range(n):
        x = int(input())
        a.append(x)
    print(QuickSort(a))"""