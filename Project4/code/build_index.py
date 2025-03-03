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

    stemmed_index = {}
    lemmatized_index = {}
    total_docs = len(documents)
    stemmed_index['total_documents'] = total_docs
    lemmatized_index['total_documents'] = total_docs
    for docID, original_text in documents.items():
        tokens = tokenize(original_text)
        
        stemmed_tokens = normalize(tokens, method='stemming')
        # Calculate frequency of each token in the document before adding to the index
        stemmed_tokens_freq = {token: stemmed_tokens.count(token) for token in set(stemmed_tokens)}
        for token, freq in stemmed_tokens_freq.items():
            if token not in stemmed_index:
                stemmed_index[token] = {'DF': 0, 'TF': []}
            stemmed_index[token]['DF'] += 1
            stemmed_index[token]['TF'].append((docID, freq))
        
        lemmatized_tokens = normalize(tokens, method='lemmatization')
        # Calculate frequency of each token in the document before adding to the index
        lemmatized_tokens_freq = {token: lemmatized_tokens.count(token) for token in set(lemmatized_tokens)}
        for token, freq in lemmatized_tokens_freq.items():
            if token not in lemmatized_index:
                lemmatized_index[token] = {'DF': 0, 'TF': []}
            lemmatized_index[token]['DF'] += 1
            lemmatized_index[token]['TF'].append((docID, freq))

    return {'stemmed_index': stemmed_index, 'lemmatized_index': lemmatized_index}




def write_index(collection, index):
    '''
    Writes the data structure to the processed folder
    '''

    assert type(index) == dict

    for index_name, index in indexes.items():
        index_file = './processed/' + collection + '_' + index_name + '.json'
        
        if os.path.exists(index_file):
            print(f"Error: The file {index_file} already exists.")
            sys.exit(1)

        with open(index_file, 'w') as file:
            json.dump(index, file)
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <collection_name>")
        sys.exit(1)

    collection_name = sys.argv[1]

    try:
        documents = read_documents(collection_name)
        indexes = build_index(documents)

        write_index(collection_name, indexes)
        print("SUCCESS")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)