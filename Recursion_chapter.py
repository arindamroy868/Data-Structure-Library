"""import turtle
my_turtle = turtle.Turtle()
my_win = turtle.Screen()"""
import timeit
# Base conversion without stack and then to string
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    #Base case
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


def reverse_string(string_list):
    #Base case
    if len(string_list) == 1:
        return string_list
    else:
        return string_list[len(string_list) - 1 ] + reverse_string(string_list[:-1])

def check_palindrome(string_input):
    string_without_spaces = "".join(list(string_input.split()))
    reversed_string = reverse_string(string_without_spaces)
    return string_without_spaces == reversed_string


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


def tree(branch_len, t):
    if branch_len > 5:
        t.down()
        if branch_len <30:
            t.color("red")
        t.forward(branch_len)
        t.right(15)
        tree(branch_len - 15, t)
        t.left(30)
        tree(branch_len - 15, t)
        t.right(15)
        tree(branch_len - 15, t)
        t.up()
        t.backward(branch_len)

"""def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    tree(45, t)
    my_win.exitonclick()"""

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + reverse_list(lst[:-1])

def fibonacci_iterative(n):
    if n ==0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        a = 0 
        b = 1
        l = [0,1]
        while n>1:
            b,a = (b+a),b
            l.append(b)
            n-=1
        return l

def fibonacci_recurrsive(n):
    if n == 0:
        return [0]
    elif n==1:
        return [0,1] 
    else:
        f = fibonacci_recurrsive(n-1)
        x = f[-1] + f[-2]
        f.append(x)
        return f


if __name__ == "__main__":
    pass