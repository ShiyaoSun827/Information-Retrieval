'''
Compares the output of print_document.py on document #30 of CISI
'''

import sys
import subprocess

print("Testing output of print_document -- expected to FAIL")

doc = "In a NN with one hidden layer using ReLU activation and a linear output layer, the activations are aggregated to form the CPWL target function. Each unit of the hidden layer is responsible for a linear piece. essay." 

program = "./code/print_document.py"
collection = "bad1"
docID = "1"

output = subprocess.check_output(["python3", program, collection, docID])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_doc1 = doc.strip().split()

if len(words_doc1) == len(words_answer):
    for i in range(len(words_answer)):
        if words_doc1[i] != words_answer[i]:
            #print("words_doc30[i]",words_doc1[i])
            #print("words_answer[i]",words_answer[i])
            print("FAIL")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned document is not as expected
#print(words_doc1)
#print("+++++++++++")
#print(words_answer)
print("FAIL")
exit(1) # signal error to OS