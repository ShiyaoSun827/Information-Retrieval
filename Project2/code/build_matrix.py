'''

Reads all documents in the collection file into memory and writes
term-document incidence matrix to the processed folder.

The program will be run from the root of the repository.

'''

import sys
import os
import json
import preprocessing
def read_documents(collection):
    extension = '.ALL'
    corpus_file = './collections/' + collection + extension

    if not os.path.exists(corpus_file):
        raise FileNotFoundError(f"No such file: {corpus_file}")

    documents = {}
    with open(corpus_file, 'r') as file:
        content = file.read()
        raw_docs = content.split('.I ')[1:]  

    for raw_doc in raw_docs:
        sections = raw_doc.split('\n.')
        doc_id = sections[0].strip()
        text_content = next((section[2:].strip() for section in sections if section.startswith('W')), '')
        documents[doc_id] = text_content

    print(f'{len(documents)} documents read in total')
    return documents

def build_incidence_matrix(documents):
    matrix = {'_M_': len(documents)}
    tokenized = {}
    all_terms = set()

    for docID, text in documents.items():
        tokenized_text = preprocessing.normalize(preprocessing.tokenize(text))
        tokenized[docID] = tokenized_text
        all_terms.update(tokenized_text)

    for term in all_terms:
        matrix[term] = [1 if term in tokenized[docID] else 0 for docID in documents]

    return matrix

def custom_json_serialize(matrix):
    parts = ['{']
    for key, value in matrix.items():
        if isinstance(value, list):
            value_str = "[" + ", ".join(map(str, value)) + "]"
        else:
            value_str = str(value)
        
        parts.append(f'    "{key}": {value_str},')
    
    if parts[-1].endswith(','):
        parts[-1] = parts[-1][:-1]
    
    parts.append('}')
    return '\n'.join(parts)

def write_matrix(collection, matrix):
    matrix_file = './processed/' + collection + '.matrix.json'

    if os.path.exists(matrix_file):
        raise FileExistsError(f"File already exists: {matrix_file}")

    matrix_json = custom_json_serialize(matrix)
    with open(matrix_file, 'w') as file:
        file.write(matrix_json)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <collection_name>")
        sys.exit(1)

    collection_name = sys.argv[1]
    try:
        documents = read_documents(collection_name)
        matrix = build_incidence_matrix(documents)
        write_matrix(collection_name, matrix)
        print("SUCCESS")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

