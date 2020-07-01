# Fibonacci series with dynamic programming
# Dictionary to store calculated results
fibonacci_dict = {0:0,1:1}
# Function to get only the final output
def fibonacci(n):
    if n==0 or n==1:
        return fibonacci_dict[n]
    else:
        if n in fibonacci_dict:
            return fibonacci_dict[n]
        else:
            fibonacci_dict[n] = fibonacci(n-1) + fibonacci(n-2)
            return fibonacci_dict[n]

# Function to get the series
def get_fibonacci_series(n):
    fibonacci(n)
    for i in fibonacci_dict:
        print(fibonacci_dict[i],end=" ")


def fibonacci2(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
import timeit
from timeit import Timer
def driver():
    t1 = Timer("fibonacci(500)","from __main__ import fibonacci")
    t2 = Timer("fibonacci2(500)","from __main__ import fibonacci2")
    print("Time taken by dp"+str(t1.timeit(number=99999999))+ "in milliseconds \n")
    print("Time taken by non-dp"+ str(t2.timeit(number=99999999)) + "in milliseconds \n")

driver()