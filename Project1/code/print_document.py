'''

Prints the *contents* of a document, as in the corpus, but read from 
a processed file.

The program will be run from the root of the repository.

'''

import sys,os
import json

# Suggestion: keep the documents in a dictionary, using the ID as the key
documents = {}

def read_documents(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    #corpus_file = './processed/' + collection + extension

    # TODO: fill in the rest
    extension = '.documents'  # Assuming the processed files have a .txt extension
    corpus_file = './processed/' + collection + extension
    if not os.path.exists(corpus_file):
        raise Exception(f"Processed file for {collection} does not exist.")

    
        
    with open(corpus_file, 'r') as file:
        doc_data = file.read().split('\n\n')
        for entry in doc_data:
            lines = entry.split('\n')
            
            
            doc_id = lines[0]
            if doc_id =='':
                break
            content = eval(lines[1])
            #print(doc_id)
            
            documents[doc_id] = {
                "title": content['title'],
                "author": content["author"],
                "abstract": content["abstract"],
                "references": content["references"]
            }
                
                
              
        
  

    '''
    with open(corpus_file, 'r') as file:
        # Example processing, adjust according to your file format
        for line in file:
            doc_id, content = line.strip().split(None, 1)
            documents[doc_id] = content
    '''


def retrieve_document(docID):
    '''
    Returns a document given its id
    '''

    # TODO: check for errors
    
        
    #return documents[docID]
    if docID in documents:
        doc_info = documents[docID]
        # Format the document content for display
        #document_content = f"Title: {doc_info['title']}\n"
        #document_content += f"Author: {doc_info['author']}\n"
        #document_content += f"Abstract: {doc_info['abstract']}\n"
        #document_content += f"References: {doc_info['references']}"
        document_content = f"{doc_info['abstract']}"
        return document_content
    else:
        return "Document not found."



if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: read document ID from command line
    # TODO: check for invalid parameters
    # TODO: print the document to STDOUT

    if len(sys.argv) != 3:
        print("Usage: python print_document.py <collection_name> <document_id>")
        sys.exit(1)
    try:
        collection_name = sys.argv[1]
        document_id = sys.argv[2]

        read_documents(collection_name)
        document_content = retrieve_document(document_id)

        print(document_content)
    except Exception as e:
        print(f"Error: {e}")

    exit(0)