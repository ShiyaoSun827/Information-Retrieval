'''
(1) calls query.py on your good collection once for each of the ten queries you created by hand; 
(2) checks that your program returns the correct answer for each query. You must test all possible scoring schemes for documents.
'''

import subprocess
import sys
import os
print("Testing output of query -- expected to PASS")


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




def run_test_query(collection_name, schemes):
    all_pass = 0
    for scheme in schemes:
        answers_test = {}
        for key, value in queries.items():
            command = ['python3', './code/query.py', collection_name, scheme, "10", value]
            try:
                result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                answers_test[key] = result.stdout.strip()
            except:
                print("FAIL")
                sys.exit(1)
        for key, value in answers_test.items():
            answers_test[key] = value.split('\n')

        trans_answer = {}
        for key, value_list in answers_test.items():
            transf_values = [pair.split(':')[0] for pair in value_list[0].split('\t')]
            trans_answer[key] = transf_values 
        all_exist = all(set(trans_answer[key]).issubset(set(answers[key])) for key in trans_answer if key in answers)
        if all_exist:
            all_pass += 1
            if all_pass == 8:
                print("PASS")
        else:
            print("FAIL")
            sys.exit(1)

if __name__ == "__main__":
    test_collection_name = 'good'
    try:
        command_matrix = ['python3', './code/build_index.py', test_collection_name]  
        result1 = subprocess.run(command_matrix, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print("FAIL")
        sys.exit(1)
    try:
        read_queries(test_collection_name, '.QRY')
        read_answers(test_collection_name, '.REL')
    except:
        print("FAIL")
        sys.exit(1)

    scoring_schemes = ["nnn", "ltn", "lnn", "ntn", "nnc", "ltc", "lnc", "ntc"]
    run_test_query(test_collection_name, scoring_schemes)