n = int(input())
def fact(n):
	factorial = 1
	if n == 0:
		return 1
	else:
		return n*(fact(n-1))

print(fact(n))