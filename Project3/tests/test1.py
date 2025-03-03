'''
(1) calls build_index.py on your good collection; 
(2) reads the corresponding inverted index file(s) in processed; 
(3) compares the inverted index read to another one, hard-coded inside test1.py, that you created by hand for your good collection. 
Your hard-coded index must be correct and the index read from the files must contain the same information.
'''

import subprocess
import sys
import json
print("Testing output of build_index -- expected to PASS")
index={"total_documents": 5, "jenna": {"DF": 1, "TF": [["1", 1]]}, "like": {"DF": 5, "TF": [["1", 1], ["2", 1], ["3", 1], ["4", 1], ["5", 1]]}, "play": {"DF": 4, "TF": [["1", 1], ["2", 2], ["3", 1], ["4", 1]]}, "tenni": {"DF": 3, "TF": [["1", 1], ["2", 1], ["3", 1]]}, "fli": {"DF": 1, "TF": [["1", 1]]}, "on": {"DF": 1, "TF": [["1", 1]]}, "the": {"DF": 1, "TF": [["1", 1]]}, "moon": {"DF": 1, "TF": [["1", 1]]}, "and": {"DF": 5, "TF": [["1", 1], ["2", 1], ["3", 1], ["4", 1], ["5", 1]]}, "swim": {"DF": 3, "TF": [["1", 1], ["4", 1], ["5", 1]]}, "lap": {"DF": 3, "TF": [["1", 1], ["4", 1], ["5", 1]]}, "but": {"DF": 5, "TF": [["1", 1], ["2", 1], ["3", 1], ["4", 1], ["5", 1]]}, "dislik": {"DF": 5, "TF": [["1", 1], ["2", 1], ["3", 1], ["4", 1], ["5", 1]]}, "run": {"DF": 3, "TF": [["1", 1], ["3", 1], ["5", 1]]}, "marathon": {"DF": 3, "TF": [["1", 1], ["3", 1], ["5", 1]]}, "marco": {"DF": 1, "TF": [["2", 1]]}, "travel": {"DF": 2, "TF": [["2", 1], ["4", 1]]}, "to": {"DF": 2, "TF": [["2", 1], ["4", 1]]}, "europ": {"DF": 2, "TF": [["2", 1], ["4", 1]]}, "row": {"DF": 2, "TF": [["2", 1], ["4", 1]]}, "in": {"DF": 4, "TF": [["2", 1], ["3", 1], ["4", 1], ["5", 1]]}, "team": {"DF": 2, "TF": [["2", 1], ["4", 1]]}, "soccer": {"DF": 2, "TF": [["2", 1], ["4", 1]]}, "lili": {"DF": 1, "TF": [["3", 1]]}, "cycl": {"DF": 2, "TF": [["3", 1], ["5", 1]]}, "race": {"DF": 2, "TF": [["3", 1], ["5", 1]]}, "evan": {"DF": 1, "TF": [["4", 1]]}, "sophia": {"DF": 1, "TF": [["5", 1]]}}
def run_read_corpus(collection_name):
    try:
        command = ['python3', './code/build_index.py', collection_name]  
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print("FAIL")
        exit(1)
    file_path = './processed/good.json'
    try:
        with open(file_path, 'r') as file:
            index_test = json.load(file)
    except FileNotFoundError:
        print("FAIL")
        exit(1)
    except json.JSONDecodeError:
        print("FAIL")
        exit(1)

    except Exception as e:
        print("FAIL")
        exit(1)

    if index == index_test:
        print("PASS")
        exit(0)

    else:
        print("FAIL")
        exit(1)
        
if __name__ == "__main__":
    test_collection_name = 'good' 
    run_read_corpus(test_collection_name)
    
