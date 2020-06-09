from StackList import stack
import string

def tobinary(num):
    s = stack()
    output = []
    while num>0:
        remainder = (num%2)
        s.push(str(remainder))
        num = num//2
    while not s.is_empty():
        output.append(s.pop())
    return "".join(output)

def tooctal(num):
    s = stack()
    output = []
    while num>0:
        remainder = (num%8)
        s.push(str(remainder))
        num = num//8
    while not s.is_empty():
        output.append(s.pop())
    return "".join(output)

def tohexadecimal(num):
    s = stack()
    output = []
    digits = '0123456789ABCDEF'
    while num>0:
        remainder = (num%16)
        s.push(str(digits[remainder]))
        num = num//16
    while not s.is_empty():
        output.append(s.pop())
    return "".join(output)

def toany(num,base):
    s = stack()
    output = []
    digits = '0123456789' + string.ascii_uppercase
    while num>0:
        remainder = (num%base)
        s.push(str(digits[remainder]))
        num = num//base
    while not s.is_empty():
        output.append(s.pop())
    return "".join(output)   

#Driver Function
"""
def main():
    a = 12
    print(toany(969,56))
    
if __name__ == "__main__":
    main()
"""