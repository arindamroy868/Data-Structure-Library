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

