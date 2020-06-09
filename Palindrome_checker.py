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
    first_half = input_string[0:len(input_string)//2]
    second_half = input_string[len(input_string)//2+1:]
    second_half = second_half[::-1]
    return first_half == second_half
