'''

Reads in a collection and a Boolean query and prints to STDOUT
the IDs of documents in the collection satisfying the query expression.

The program will be run from the root of the repository.

'''

import sys
import preprocessing # implements tokenize and normalize text
import precedence # implements the functions to fix precedece
import json
import argparse

'''
Below are the implementation of the basic boolean operators on bit vectors
'''
def term_vector(term):
    '''
    if term not in matrix or len(matrix[term]) != matrix['_M_']:
        raise Exception("Invalid query expression OR Out-Of-Vocabulary")  
    return matrix[term]
    '''
    if term not in matrix:
        raise Exception(f"Error: Term  is not in the vocabulary.")
    elif len(matrix[term]) != matrix['_M_']:
        raise Exception(f"Error: Length mismatch for term '{term}' vector.")
    return matrix[term]
    



def AND(vector1, vector2):
    assert len(vector1) == len(vector2) == matrix['_M_']
    return [a and b for a, b in zip(vector1, vector2)]

def OR(vector1, vector2):
    assert len(vector1) == len(vector2) == matrix['_M_']
    return [a or b for a, b in zip(vector1, vector2)]

def NOT(vector):
    assert len(vector) == matrix['_M_']
    return [not a for a in vector]


'''
Below are the other key functions for the assignment.
'''

def read_matrix(collection):
    global matrix
    matrix_path = f'./processed/{collection}.matrix.json'
    try:
        with open(matrix_path, 'r') as file:
            matrix = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{matrix_path}' does not exist.")
        sys.exit(1)
    return matrix



def document_ids(vector):
    '''
    Returns a list with the IDs of documents corresponding to non-zero entries 
    in the matrix. Raises an Exception if all entries are zero.
    '''
    assert len(vector) == matrix['_M_']
    ids = [i+1 for i, value in enumerate(vector) if value]
    return ids

'''
def solve_expression(stack):
    while len(stack) > 1:  
        right = stack.pop()
        operator = stack.pop()
        if len(stack) == 0 and operator == ':not:':  
            stack.append(NOT(right))
            continue
        elif len(stack) == 0:
            raise Exception("Malformed expression: Stack is empty before operation can be applied.")
        left = stack.pop()
        if operator == ':and:':
            stack.append(AND(left, right))
        elif operator == ':or:':
            stack.append(OR(left, right))
        else:
            raise Exception(f"Error: Unrecognized operator '{operator}' in expression.")
    return stack[0]
    '''
def check_neighboring_parentheses(expr_list):
   
    # Iterate through the list, except the last element to avoid index out of range
    for i in range(len(expr_list) - 1):
        # Check for both conditions
        if (expr_list[i] == '(' and expr_list[i + 1] == ')') or (expr_list[i] == ')' and expr_list[i + 1] == '('):
            return True  # Return True immediately if a neighboring pair is found
    return False

def solve_expression(stack):
    if not stack:
        raise Exception("Error: Empty expression stack when solving.")
    while len(stack) > 1:
        try:
            right = stack.pop()
            operator = stack.pop()
            if operator == ':not:':  # :not: is unary, handle differently
                left = None  # There's no left operand for :not:
            else:
                left = stack.pop()
        except IndexError:  # empty stack issues
            
            raise Exception("Error: Malformed expression: Stack is empty before operation can be applied.It may cased by operators or missing blanks")
        
        if operator == ':and:':
            stack.append(AND(left, right))
        elif operator == ':or:':
            stack.append(OR(left, right))
        elif operator == ':not:':
            stack.append(NOT(right))  # Apply :not: only to the right as it's unary
        else:
            raise Exception(f"Error: Unrecognized operator '{operator}' in expression.")
    return stack[0]






def answer(tokenized_query):
    
    stack = []
    for token in tokenized_query:
        if token in (':and:', ':or:', ':not:'):
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            expr = []
            while stack[-1] != '(':
                expr.insert(0, stack.pop())
            stack.pop()
            stack.append(solve_expression(expr))
        else:
            stack.append(term_vector(token))
    return document_ids(solve_expression(stack))



def tokenize_and_answer(query_expression):
    '''
    Takes a query expression (string), tokenizes it, calls fix_precedence to
    add parenthesis as discussed in class, and calls answer to solve the
    query and return the ids.
    '''
    assert type(query_expression) == str
    if check_neighboring_parentheses(query_expression.split()):
        raise Exception("Error: There exists Misplaced parenthesis")
    fixed_precedence = precedence.fix_precedence(query_expression.split())
    
    #print("fixed_precedence: ", fixed_precedence)
    tokenized_query = []

    reserved = set(['(', ')', ':and:', ':or:', ':not:'])
    
    for token in fixed_precedence:
        if token in reserved:
            tokenized_query.append(token)
        else:
            # note: tokenize/normalize work with lists but we expect a single word here
            terms = preprocessing.normalize(preprocessing.tokenize(token))
            assert len(terms) == 1
            tokenized_query.append(terms[0])
    return answer(['('] + tokenized_query + [')'])


matrix = {}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script.py <collection_name> <query_expression>")
        sys.exit(1)
    try:
        collection_name = sys.argv[1]  
        query_expression = " ".join(sys.argv[2:]) 
        matrix = read_matrix(collection_name)
        for docID in tokenize_and_answer(query_expression):
            print(docID)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
