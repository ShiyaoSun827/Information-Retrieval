'''

Implements the functions to "fix" the precendence of operators in the 
query expression provided by the user by "wrapping" higher precedence
subexpressions in parenthesis, making sure that:

1. parenthesis provided by the user are left untouched.
2. :not: operators are "fixed" first.
3. :and: expressions are "fixed" next.

'''

def find_par_exp_forward(expression):
    '''
    Finds the index of the token within expression correspondin to the end of 
    the parenthetical expression in front of a :not: or an :and: operator.
    '''
    assert type(expression) == list
    depth = 0
    
    for i, token in enumerate(expression):
        if token == '(':
            depth += 1
        elif token == ')':
            depth -= 1
            if depth == 0:
                return i
    raise ValueError("Parenthesis mismatch in the forward direction")
    

def find_par_exp_backward(expression):
    '''
    Finds the index of the token within expression correspondin to the start of 
    the parenthetical expression behind an :and: operator.
    '''
    assert type(expression) == list
    depth = 0
    for i in range(len(expression)-1, -1, -1):  # Iterate backwards
        if expression[i] == ')':
            depth += 1
        elif expression[i] == '(':
            depth -= 1
            if depth == 0:
                return i
    raise ValueError("Parenthesis mismatch in the backward direction")


def fix_precedence_NOT(expression):
    '''
    Finds and "wraps" all :not: exp in the query expression as discussed in class.
    '''
    
    assert isinstance(expression, list), "Expression must be a list"
    i = 0
    while i < len(expression):
        if expression[i] == ':not:':
            #first, count the elements after the not,
            temp = i + 1
            left_wrap_count = 0
            right_wrap_count = 0
            words_count = 0
            stop = False
            Single = False
            while temp < len(expression) and not stop:
                if expression[temp] == '(' and right_wrap_count == 0 and  left_wrap_count==0:
                    left_wrap_count += 1
                    #print("left_wrap_count",temp)

                elif expression[temp] == '(' and right_wrap_count < left_wrap_count:
                    left_wrap_count+=1
                    #print("left_wrap_count",temp)
                elif expression[temp] == ')' and right_wrap_count < left_wrap_count:
                    right_wrap_count += 1
                    #print("right_wrap_count",temp)
                elif expression[temp] == ':and:' or expression[temp] == ':or:':
                    if temp - i == 2:
                        stop = True
                        Single = True
                    else:
                        words_count+=1
                else:
                    words_count += 1
                    #print("words_count",temp)
                if right_wrap_count != 0 and  left_wrap_count!=0 and right_wrap_count == left_wrap_count:
                    stop = True
                else:
                    temp+= 1
            if Single:
                total = 1
            else:

                total = left_wrap_count + right_wrap_count + words_count
            #print(total)
            expression.insert(i, '(')
            end_idx = i + total + 2
            expression.insert(end_idx, ')')
            i = i + 2
            




          
        else:
            i += 1  # Move to the next element if current is not ':not:'
    #print("done",expression)
    return expression
   


def fix_precedence_AND(expression, start=0):
    '''
    Finds and "wraps" all exp1 :and: exp2 in the query expression as discussed in class.
    '''
    assert isinstance(expression, list), "Expression must be a list"
    i = start
    while i < len(expression):
        if expression[i] == ':and:':
            # Initialize variables to track parentheses and words around ':and:'
            left_wrap_count = 0
            right_wrap_count = 0
            words_count = 0
            temp = i - 1  # Start from the term before ':and:'
            single = False
            stop = False

            # Count elements before :and:
            while temp >= 0 and not stop:
                if expression[temp] == ')' and left_wrap_count == 0:
                    right_wrap_count += 1
                elif expression[temp] == ')' and left_wrap_count < right_wrap_count:
                    right_wrap_count += 1
                elif expression[temp] == '(' and left_wrap_count < right_wrap_count:
                    left_wrap_count += 1
                else:
                    words_count += 1
                if left_wrap_count != 0 and left_wrap_count == right_wrap_count:
                    stop = True  # Stop if matching parentheses are found
                else:
                    temp -= 1
            if single:
                total = 1
            else:

                total = left_wrap_count + right_wrap_count + words_count
            

            # Encapsulate left part with '(' if needed
            if left_wrap_count == 0 or left_wrap_count != right_wrap_count:
                #expression.insert(i - words_count, '(')  # Insert '(' before the left expression
                i += 1  # Adjust index due to new insertion

            # Reset counters for right side
            temp = i + 1  # Start from term after ':and:'
            left_wrap_count = 0
            right_wrap_count = 0
            words_count = 0

            # Count elements after :and:
            while temp < len(expression):
                if expression[temp] == '(' and right_wrap_count == 0:
                    left_wrap_count += 1
                elif expression[temp] == '(' and right_wrap_count < left_wrap_count:
                    left_wrap_count += 1
                elif expression[temp] == ')' and right_wrap_count < left_wrap_count:
                    right_wrap_count += 1
                elif expression[temp] not in (':and:', ':or:', '(', ')'):
                    words_count += 1  # Increment for words/terms
                if right_wrap_count != 0 and left_wrap_count == right_wrap_count:
                    break  # Stop if matching parentheses are found
                temp += 1

            # Encapsulate right part with ')' if needed
            if right_wrap_count == 0 or left_wrap_count != right_wrap_count:
                #expression.insert(i + 1 + words_count, ')')  # Insert ')' after the right expression
                i += 1  # Adjust index due to new insertion

        i += 1  # Proceed to next element

    return expression
    
   

def fix_precedence(expression):
    '''
    Fixes the precedence of an entire expression
    '''
    
    assert type(expression) == list
    step1 = fix_precedence_NOT(expression)
    step2 = fix_precedence_AND(step1)
    
    return step2