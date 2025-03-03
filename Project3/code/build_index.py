'''

Reads all documents in the collection file into memory and writes
an inverted index to the processed folder.

The program will be run from the root of the repository.

'''

import sys
import json
import os
from preprocessing import tokenize
from preprocessing import normalize


def read_documents(collection):
    '''
    Reads the documents in the collection (inside the 'collections' folder).
    '''

    assert type(collection) == str
    corpus_file = './collections/' + collection + '.ALL'

    documents = {}


    try:
        with open(corpus_file, 'r') as file:
            content = file.read().strip()
            if not content:
                raise ValueError("The collection file is empty.")
            docs = content.split('.I')[1:]
            for doc in docs:
                parts = doc.split('\n', 1)
                if len(parts) < 2:
                    continue

                docID = parts[0].strip()
                if not docID.isdigit():
                    pass
                else:
                    if '.W' not in parts[1]:
                        raise ValueError(f"Collection {collection} document ID {docID} is missing a content section (.W).")
                    else:
                        _, docText = parts[1].split('.W', 1)
                        if docID in documents:
                            raise ValueError(f"Collection {collection} duplicate document ID {docID} found.")
                        documents[docID] = docText.strip() 

    except FileNotFoundError:
        print(f"Error: The file {corpus_file} does not exist.")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

    print(f'{len(documents)} documents read in total')
    return documents


def build_index(documents):
    '''
    Builds inverted index.
    '''
    assert type(documents) == dict

    index = {}
    
    for docID, original_text in documents.items():

        tokens = normalize(tokenize(original_text))
        term_frequency = {}
        for token in tokens:
            if token in term_frequency:
                term_frequency[token] += 1
            else:
                term_frequency[token] = 1

        for term, freq in term_frequency.items():
            if term not in index:
                index[term] = {'DF': 0, 'TF': []}
            index[term]['DF'] += 1
            index[term]['TF'].append([docID, freq])

    return index



def write_index(collection, index):
    '''
    Writes the data structure to the processed folder
    '''

    assert type(index) == dict
    extension = '.json'
    index_file = './processed/' + collection + extension
    
    if os.path.exists(index_file):
        print("SUCCESS")
        #print(f"Error: The file {index_file} already exists.")
        sys.exit(1)

    with open(index_file, 'w') as file:
        json.dump(index, file)

    

if __name__ == "__main__":
    '''
    main() function
    '''
    if len(sys.argv) != 2:
        print("Usage: python script.py <collection_name>")
        sys.exit(1)
    
    collection_name = sys.argv[1]
    
    try:
        documents = read_documents(collection_name)
        index = build_index(documents)
        
        index_with_count = {'total_documents': len(documents)}
        index_with_count.update(index)
        
        write_index(collection_name, index_with_count)
        print("SUCCESS")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
