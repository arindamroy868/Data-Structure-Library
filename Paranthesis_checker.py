from StackList import stack

# While Loop Implementation
def par_checker(input_string):
    s = stack()
    string_list = list(input_string)
    balanced = True
    index = 0
    while index<len(string_list) and balanced:
        token = string_list[index]
        # If token is equal to '(' then pushed into stack
        if token == "(":
            s.push(token)
        # If token is equal to ')' then popped the top element if stack is not empty
        else:
            if not s.is_empty():
                s.pop()
            # Since Stack is not empty There must be atleast one '(' symbol less in string of tokens so Paranthesis is not balanced so break the loop
            else:
                balanced = False
        index += 1
    # If loop was ended after complete iteration of tokens and the stack is empty then the parathesis is balanced else there must be more no of '(' compared to no of ')' symbols
    if s.is_empty() and balanced:
        return True
    else:
        return False

#For loop Implementation
def par_checker2(input_string):
    s = stack()
    string_list = list(input_string)
    for i in string_list:
        # If token is equal to '(' then pushed into stack
        if i == '(':
            s.push(i)
        # If token is equal to ')' then popped the top element if stack is not empty
        else:
            # Since Stack is not empty There must be atleast one '(' symbol less in string of tokens so Paranthesis is not balanced so break the loop
            if not s.is_empty():
                s.pop()
            else:
                break
    # If loop was ended after complete iteration of tokens and the stack is empty then the parathesis is balanced else there must be more no of '(' compared to no of ')' symbols
    else:
        if not s.is_empty():
            return False
        else:
            return True
    # If the loop was ended before complete iteration that means the paranthesis is not balanced
    return False

# While Loop Implementation for every type of paranthesis '{} [] ()'
def par_checker3(input_string):
    s = stack()
    string_list = list(input_string)
    balanced = True
    index = 0
    print(string_list)
    while index<len(string_list) and balanced:
        token = string_list[index]
        left_par = '([{'
        right_par = ')]}'
        
        if token in left_par:
            s.push(token)
        else:
            if not s.is_empty():
                top = s.pop()
                balanced = left_par.index(top) == right_par.index(token)
            else:
                balanced = False
        index += 1
    if s.is_empty() and balanced:
        return True
    else:
        return False

# For Loop Implementation for every type of paranthesis '{} [] ()'
def par_checker4(input_string):
    s = stack()
    string_list = list(input_string)
    left_par ='([{'
    right_par = ')]}'

    for token in string_list:    
        if token in left_par:
            s.push(token)   
        else:
            if not s.is_empty():
                top = s.pop()
                if not left_par.index(top) == right_par.index(token):
                    break
            else:
                break
    else:
        if not s.is_empty():
            return False
        else:
            return True
    return False


