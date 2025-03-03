'''
Compares the output of print_document.py on document #30 of CISI
'''

import sys
import subprocess

print("Testing output of print_document -- expected to PASS")

doc30 = "   The rationale is given for creation and maintainance by an information " \
" center of a controlled indexing and retrieval vocabulary.. Basic vocabulary" \
" principles are (1) use of natural language, (2) development of hospitality" \
" to new concepts, (3) provision of adequate cross-referencing, and (4)" \
" formatting for easy use.. Terminalogical conventions necessary for development" \
" and control of a useful vocabulary are summarized, and the techniques for " \
" applying these conventions to construct a thesaurus are described.. " \
" Computerized editing techniques and updating techniques are briefly set forth.." 

program = "./code/print_document.py"
collection = "CISI"
docID = "30"

output = subprocess.check_output(["python3", program, collection, docID])
answer = output.decode('utf-8').strip()

# compare outputs, word by word
words_answer = answer.split()
words_doc30 = doc30.strip().split()

if len(words_doc30) == len(words_answer):
    for i in range(len(words_answer)):
        if words_doc30[i] != words_answer[i]:
            print("words_doc30[i]",words_doc30[i])
            print("words_answer[i]",words_answer[i])
            print("FAIL")
            exit(1) # signal error to OS

    # if we reach this point, the answer is correct
    print("PASS")
    exit(0) # signal success to OS

# if we reach this point, the returned document is not as expected
print(words_doc30)
print("+++++++++++")
print(words_answer)
print("FAIL")
exit(1) # signal error to OS