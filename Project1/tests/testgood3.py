'''
Compares the output of print_answers on query #82 of CISI
'''

import sys
import subprocess

print("Testing output of print_answers -- expected to PASS")

answer5 = set([2]) 
program = "./code/print_answers.py"
collection = "good"
query = "5"

output = subprocess.check_output(["python3", program, collection, query])
answer = output.decode('utf-8').strip()

# compare outputs, id by id
ids_answer = [int(x) for x in answer.split()]

if len(answer5) == len(ids_answer):
    for i in range(len(ids_answer)):
        if ids_answer[i] not in answer5:
            print("FAIL")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned answer is not as expected
print("FAIL")
exit(1) # signal error to OS
