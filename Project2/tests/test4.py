'''
(1) calls query.py on CISI_bool collection once for each query in CISI_bool.QRY; 
(2) checks the answer provided in CISI_bool.REL is identical to what your program finds.
'''

import subprocess
import sys
import os
print("Testing output of query on CISI_bool -- expected to PASS")


queries = {}
def read_queries(collection, extension):
    queries_file = './collections/' + collection + extension
    if not os.path.exists(queries_file):
        raise FileNotFoundError(f"The file {queries_file} does not exist.")

    with open(queries_file, 'r') as file:
        query_id = ''
        query_text = ''
        found_w = True

        for line in file:
            if line.startswith('.I'):
                new_query_id = line.split()[1]
                if query_id:
                    #if not found_w:
                        #raise ValueError(f"{collection + extension}: Missing required '.W' section in query {query_id}")
                    if query_id in queries:
                        raise ValueError(f"{collection + extension}: Duplicate ID {query_id}")
                    queries[query_id] = query_text.strip()
                if new_query_id in queries:
                    raise ValueError(f"{collection + extension}: Duplicate ID {new_query_id}")
                query_id = new_query_id
                query_text = ''
                #found_w = False
            elif line.startswith('.W'):
                #if found_w:
                    #raise ValueError(f"{collection + extension}: Duplicated '.W' section in query {query_id}")
                found_w = True
            else:
                if found_w:
                    query_text += line

        if query_id:
            #if not found_w:
                #raise ValueError(f"{collection + extension}: Missing required '.W' section in query {query_id}")
            if query_id in queries:
                raise ValueError(f"{collection + extension}: Duplicated ID {query_id}")
            queries[query_id] = query_text.strip()

answers = {}
def read_answers(collection, extension):

    answers_file = './collections/' + collection + extension
    if not os.path.exists(answers_file):
        raise FileNotFoundError(f"The file {answers_file} does not exist.")

    with open(answers_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 2:
                raise ValueError(f"{collection}{extension}: Missing required sections in document {line}")

            query_id, doc_id = parts[0], parts[1]
            if query_id in answers and doc_id in answers[query_id]:
                raise ValueError(f"Duplicate document ID {doc_id} found for query ID {query_id}")

            if query_id not in answers:
                answers[query_id] = []
            answers[query_id].append(doc_id)



def run_test_query(collection_name):
    answers_test = {}
    for key, value in queries.items():
        command = ['python3', './code/query.py', collection_name, value]
        
        try:
            result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            answers_test[key] = result.stdout.strip()
           
        except:
            print("FAIL")
            sys.exit(1)
    for key, value in answers_test.items():
        answers_test[key] = value.split('\n')
    if answers == answers_test:
        print("PASS")
        sys.exit(0)
    else:
        print("FAIL")
        sys.exit(1)

if __name__ == "__main__":
    test_collection_name = 'CISI_bool'
    try:
        command_matrix = ['python3', './code/build_matrix.py', test_collection_name]  
        result1 = subprocess.run(command_matrix, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print("CISI_bool Matrix already exists")

    try:
        read_queries(test_collection_name, '.QRY')
        read_answers(test_collection_name, '.REL')
        
      
        
    except Exception as e:
        print("FAIL",e)
        sys.exit(1)

    run_test_query(test_collection_name)