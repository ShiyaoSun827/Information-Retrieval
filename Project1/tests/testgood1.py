'''
Compares the output of print_document.py on document #30 of CISI
'''

import sys
import subprocess

print("Testing output of print_document -- expected to PASS")

doc3 = 'The defining features of a "cause and effect" essay are causal chains that connect from a cause to an effect, careful language, and chronological or emphatic order. A writer using this rhetorical method must consider the subject, determine the purpose, consider the audience, think critically about different causes or consequences, consider a thesis statement, arrange the parts, consider the language, and decide on a conclusion.' 

program = "./code/print_document.py"
collection = "good"
docID = "3"

output = subprocess.check_output(["python3", program, collection, docID])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_doc3 = doc3.strip().split()

if len(words_doc3) == len(words_answer):
    for i in range(len(words_answer)):
        if words_doc3[i] != words_answer[i]:
            #print("words_doc30[i]",words_doc30[i])
            #print("words_answer[i]",words_answer[i])
            print("FAIL")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned document is not as expected
#print(words_doc3)
#print("+++++++++++")
#print(words_answer)
print("FAIL")
exit(1) # signal error to OS