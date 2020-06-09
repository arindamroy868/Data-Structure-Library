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

