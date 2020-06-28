from Deques import deque

#Deque Method
def palindrome_check(input_string):
    d = deque()
    for x in input_string:
        d.add_rear(x)
    palindrome = True
    while d.size()>1:
        front  = d.remove_front()
        rear  = d.remove_rear()

        if front != rear:
            palindrome = False
            break
    return palindrome

#String Reversal Method
def palindrome_check2(input_string):
    reversed_string = input_string[::-1]
    return reversed_string == input_string

