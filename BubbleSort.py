def bubbleSort(l):
	for i in range(len(l)):
		for j in range(len(l)-i-1):
			if l[j]>l[j+1]:
				temp = l[j]
				l[j] = l[j+1]
				l[j+1] = temp
	print(*l,end=" ")


if __name__ == "__main__":

	n = int(input())
	l = []
	for _ in range(n):
		l.append(int(input()))
	bubbleSort(l)




