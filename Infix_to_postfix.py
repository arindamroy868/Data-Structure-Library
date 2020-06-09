from StackList import stack
import string

"""
    Algorithm For Infix to Postfix Conversion
    ------------------------------------------
    1. We have created a stack to store operators named as op_stack
    2. We have created a output_list which will store the postfix_expression
    3. We start a for loop and iterate over each symbol in the input string of infix_expression
        IN LOOP
        1. if the symbol is an operand(ie. A numeric value or a variable) then we simply append that symbol to the output list
        2. if the symbol is '(' open bracket then we push that to the op_stack named stack
        3. if the symbol is ')' close bracket then we pop symbols from op_stack and append to the output list until '(' is encoutered
        4. if the symbol is an operator '+' , '-' , '*' , '/' then we check 
                1. If op_stack is empty then simply push the operator into the stack
                else pop the top of stack and append to output list till stack is not empty or precedence of top of op_stack is not < precedence of incoming operator
        5. if op_stack is not empty then simply pop op_stack and append to output list till stack is not empty
        5. return the output list
"""
def Infix_to_postfix(infix_expression):
    # Defining Precedence Dictionary
    precedence = {'*':3,'/':3,'+':2,'-':2,'(':1,')':1}
    # Creating operator stack
    op_stack = stack()
    # Output list
    postfix_list = []
    # Input String List
    infix_list = list(infix_expression.split(" "))
    operands = string.ascii_letters 


    for symbol in infix_list:
        if symbol in operands or symbol.isnumeric():
            postfix_list.append(symbol)
        elif symbol == '(':
            op_stack.push(symbol)
        elif symbol == ')':
            if op_stack.is_empty():
                return "Invalid infix expression"
            else:
                popped_symbol = op_stack.pop()
                while popped_symbol != '(':
                    postfix_list.append(popped_symbol)
                    if op_stack.is_empty(): 
                        return "Invalid infix expression"
                    popped_symbol = op_stack.pop()
        else:
            while not op_stack.is_empty() and precedence[op_stack.peek()] >= precedence[symbol]:
                postfix_list.append(op_stack.pop())
            op_stack.push(symbol)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)
#--------------------------------------------------------------------------------------------------------------------------------------------
"""
Algorithm for Infix to Prefix
1. create an operator stack named op_stack to store the operators in th stack
2. Convert the input token string into a list and reverse the list
3. Create an output list to store the result named as prefix_list
4. For each symbol in the infix_list
    1. If symbol is an operand the simply append to the prefix_list
    2. If symbol is ')' then push it into the op_stack
    3. If symbol is '(' the check if op_stack is empty or not
        if op_stack is empty then return that invalid infix expression
        else:
            pop operators from the op_stack and append to the prefix list until ')' poppes off of op_stack 
            else:
                return invalid infx expression
    4. If symbol is an operator then check if op_stack is empty or not:
        if op_stack is empty then push the symbol into op_stack
        else:
            compare the precedence of top of op_stack to the precedence of symbol:
            if precedence of top of op_stack >=  precedence of symbol then pop the op_stack and append to the prefix list until the condition becomes false or the op_stack becomes empty
    while op_stack is not empty:
        pop the op_stack and append to the prefix_list
    return the reverse of prefix_list and in string format

"""
def Infix_to_prefix(infix_expression):
    # Defining Precedence Dictionary
    precedence = {'*':3,'/':3,'+':2,'-':2,'(':1,')':1}
    # Creating operator stack
    op_stack = stack()
    # Output list
    prefix_list = []
    # Converting the input string of tokens into list
    infix_list = list(infix_expression.split(" "))
    # Reversing the list so we can simluate the processing of string from right to left 
    infix_list = infix_list[::-1]
    # Defining set of alphabets
    operands = string.ascii_letters

    for symbol in infix_list:
        if symbol in operands or symbol.isnumeric():
            prefix_list.append(symbol)
        elif symbol == ')':
            op_stack.push(symbol)
        elif symbol == '(':
            if op_stack.is_empty():
                return "Invalid infix expression"
            else:
                popped_symbol = op_stack.pop()
                while popped_symbol != ')':
                    prefix_list.append(popped_symbol)
                    if op_stack.is_empty():
                        return " Invalid infix expression" 
                    popped_symbol = op_stack.pop() 
        else:
            while not op_stack.is_empty() and precedence[op_stack.peek()] >= precedence[symbol]:
                prefix_list.append(op_stack.pop())
            op_stack.push(symbol)

    while not op_stack.is_empty():
        prefix_list.append(op_stack.pop())
    
    return " ".join(prefix_list[::-1])
    
#--------------------------------------------------------------------------------------------------------------------------------------------

"""
Algorithm for postfix evaluation
---------------------------------
1. In postfix evaluation we need to push the operand in the stack
2.if any operator is encountered pop 2 operands and perform the operation on those operands and push the result of operation into the stack
    when input string is empty pop the op_stack and return 
"""
def postfix_evaluation(postfix_expression):
    symbol_string = list(postfix_expression.split(" "))
    op_stack = stack()
    
    for symbol in symbol_string:
        if symbol.isnumeric():
            op_stack.push(symbol)
        else:
            if op_stack.size() < 2:
                return "SyntaxError: Invalid Postfix Notation"
            else:
                process(op_stack,symbol)
    return op_stack.pop()
#--------------------------------------------------------------------------------------------------------------------------------------------

"""
Algorithm for infix evaluation
------------------------------
1. Create 2 stacks one named operator_stack and another operand_stack to store operator tokens and operand symbols
2. Read the input symbol
    1. If the input symbol is and operand i.e numeric or alphabetic then push them into the operand stack
    2. If the symbol is  '(' then push it into the operator stack
    3. If the symbol is ')' then pop the symbol on top of stack and perform process(Defined in function 'process') until '(' symbol pops out of operator stack
        Process defined is:
        pop 2 operands from operator stack and perform the operation based on the operator popped off from operator stack
    4. If the symbol is an operator then check if the operator stack is empty or not, If stack is empty then simply push the symbol in operator_stack else
        compare symbol's precedence to the operator on top of operator stack
            1. if the precedence of top of operator_stack is greater than the precedence of the input operator symbol then pop the operator from operator_stack and perform the 'Process'
            2. repeat step 1 untill the precedence of top of operator_stack is not less than input symbol or the stack is empty
            3. Push  the input symbol into the operator_stack
3. While operator_stack is not empty pop the operator_stack and perform the 'Process'
pop the operand stack and return 
"""

def infix_evaluation(infix_expression):
    precedence = {'^':4,'*':3,'/':3,'+':2,'-':2,'(':1}
    infix_list = list(infix_expression.split(" "))
    # Creating 2 seprate stacks, one to store operands and another to store operators
    operator_stack = stack()
    operand_stack = stack()
    # Read the input symbol
    for token in infix_list:
        #1. If the input symbol is and operand i.e numeric or alphabetic then push them into the operand stack
        if token.isnumeric():
            operand_stack.push(token)
        #2. If the symbol is  '(' then push it into the operator stack
        elif token == '(':
            operator_stack.push(token)
        #3. If the symbol is ')' then pop the symbol on top of stack and perform process(Defined in function 'process') until '(' symbol pops out of operator stack
            #Process defined is:
            #pop 2 operands from operator stack and perform the operation based on the operator popped off from operator stack
        elif token == ')':
            top = operator_stack.pop()
            while top != '(':
                process(operand_stack,top)
                top = operator_stack.pop()
        #4. If the symbol is an operator, then check if the operator stack is empty or not, If stack is empty then simply push the symbol in operator_stack else
            # compare symbol's precedence to the operator on top of operator stack
                # 1. if the precedence of top of operator_stack is greater than the precedence of the symbol then pop the operator from operator_stack and perform the 'Process'
                # 2. repeat step 1 untill the precedence of top of operator_stack is not less than input symbol or the stack is empty
                # 3. Push  the input symbol into the operator_stack
        elif token in precedence:
            if operator_stack.is_empty():
                operator_stack.push(token)
            else:
                while not operator_stack.is_empty():
                    top = operator_stack.peek()
                    if precedence[top] > precedence[token]:
                        process(operand_stack,operator_stack.pop())
                    else:
                        break
                operator_stack.push(token)
        else:
            return "Invalid Operator Encountered"
    #3. While operator_stack is not empty pop the operator_stack and perform the 'Process'
    while not operator_stack.is_empty():
        process(operand_stack,operator_stack.pop())
    # pop the operand stack and return
    return operand_stack.pop()
#--------------------------------------------------------------------------------------------------------------------------------------------    

# Helper Function to perform mathematical operation
def math_function(a,b,symbol):
    if symbol == '^':
        return a**b
    elif symbol == '*':
        return a*b
    elif symbol == '/':
        return a/b
    elif symbol == '+':
        return a+b
    elif symbol == '-':
        return a-b
    else:
        return "Invalid Operator"

# Helper function of popping 2 elements from operand stack then performing the desired operation and then pushing the result back into the stack
def process(operand_stack,token):
    b = int(operand_stack.pop())
    a = int(operand_stack.pop())
    operand_stack.push(math_function(a,b,token))   


# Driver Function
"""if __name__ == "__main__":
    x = 'A + ( ( B + C ) * ( D + E ) )'
    print(Infix_to_prefix(x))"""