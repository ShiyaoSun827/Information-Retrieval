'''
Compares the output of print_query on query #34 of CISI
'''

import sys
import subprocess

print("Testing output of print_query -- expected to PASS")

query4 = 'Show me the features of a "cause and effect".' 

program = "./code/print_query.py"
collection = "good"
query = "4"

output = subprocess.check_output(["python3", program, collection, query])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_query4 = query4.strip().split()

if len(words_query4) == len(words_answer):
    for i in range(len(words_answer)):
        if words_query4[i] != words_answer[i]:
            print("FAIL")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned answer is not as expected
print("FAIL")
exit(1) # signal error to OS