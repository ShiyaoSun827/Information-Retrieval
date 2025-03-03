'''
 (1) calls query.py on your good collection once for each of the ten queries you created by hand; 
 (2) checks that your program returns the correct answer for each query.
'''

import subprocess
import sys
import os
import sys

# Append the directory of your module to sys.path
sys.path.append('code')
from query import read_matrix,tokenize_and_answer

print("Testing output of query -- expected to Pass")
error = {'1':'term not in vocabulary',
           '2':'misplaced parenthesis',
           '3':'missing blanks between operators',
           '4':'invalid :and: expression',
           '5':'invalid :or: expression'}
#for i in range(1, 6):
    #print("Error is : query",str(i),error[str(i)])
#term not in vocabulary:Key = 1
#misplaced parenthesis:Key = 2
#missing blanks between operators:Key = 3
#invalid :and: expression:Key = 4
#invalid :or: expression:Key = 5
#Then original query in good.QRY is:( novels :or: crowded ) :and: :not: beaches
queries = {'1':'( timhontons :or: purelife ) :and: :not: redbull',
           '2':'( novels :or: crowded ) ( :and: :not: beaches)',
           '3':'( novels :or: crowded) :and: :not: beaches',
           '4':'( novels :or: crowded ) :not: :and: beaches',
           '5':'( novels :not: :or: crowded ) :and: :not: beaches'}







            
    

if __name__ == "__main__":
    test_collection_name = 'good'
    try:
        command_matrix = ['python3', './code/build_matrix.py', test_collection_name]  
        result1 = subprocess.run(command_matrix, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        #print("good matrix already exists")
        pass
    
    error_ans = {'1':'Error: Term  is not in the vocabulary.',
           '2':'Error: There exists Misplaced parenthesis',
           '3':'Error: Malformed expression: Stack is empty before operation can be applied.It may cased by operators or missing blanks',
           '4':'Error: Malformed expression: Stack is empty before operation can be applied.It may cased by operators or missing blanks',
           '5':'Error: Malformed expression: Stack is empty before operation can be applied.It may cased by operators or missing blanks'}
    check = False
    count = 0
        
            
    matrix = read_matrix(test_collection_name)
    for i in range(1, 6):  # Assuming there are 5 queries
        try:
            docID = tokenize_and_answer(queries[str(i)])
            
        except Exception as e:
            
            if error_ans[str(i)] == str(e):
                count +=1
               
    
    if count == 5:
        print("Pass")
            
            #print("--------------------------------------------------------")
            #print("The Actual Error is:",error[str(i)])
            #print(f"FAIL: on query {i}", e)
            
    exit(1)
                    
    

   

