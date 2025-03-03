'''

Reads all documents in the collection file into memory and writes
the data structure to the processed folder.

The program will be run from the root of the repository.

'''
'''
Unique ID (.I): This is a unique identifier assigned to each document in the collection. 
It helps in uniquely distinguishing and referencing each document.

Title (.T): This part contains the title of the document. 
It gives a brief idea about the content or subject of the document.

Author (.A): This section lists the author(s) of the document. 
It provides information about who wrote or contributed to the document.

Abstract (.W): This is a summary or abstract of the document. 
It provides a concise overview of the document's content, 
giving insights into what the document is about.

List of Cross-References to Other Documents (.X): 
This part contains references to other documents within the collection, 
allowing for the establishment of relationships or links between various documents.

These elements combine to form a comprehensive representation of each document, 
making the CISI.ALL file a valuable resource for training and 
testing information retrieval models, especially 
when used in conjunction with queries from the CISI.QRY file and 
relevance judgments from the CISI.REL file​​.
'''

import sys,os

# Suggestion: keep the documents in a dictionary, using the ID as the key
documents = {}

def read_documents(collection):
    '''
    Reads the documents in the collection (inside the 'collections' folder).
    '''
    #corpus_file = './collections/' + collection + extension

    # TODO: fill in the rest and check for errors

        
    extension = '.ALL'
    corpus_file = './collections/' + collection + extension
    if not os.path.exists(corpus_file):
        raise Exception(f"File {corpus_file} does not exist.")
    
    current_doc_id = None
    current_title = ''
    current_author = ''
    current_abstract = ''
    current_references = ''
    section = None
    with open(corpus_file, 'r') as file:
        for line in file:
            if line.startswith('.I'):
                if current_doc_id is not None:
                    documents[current_doc_id] = {
                        "title": current_title.strip(),
                        "author": current_author.strip(),
                        "abstract": current_abstract.strip(),
                        "references": current_references.strip()
                    }
                current_doc_id = line.split()[1]
                current_title = current_author = current_abstract = current_references = ''
                section = None
            elif line.startswith('.T'):
                section = 'title'
            elif line.startswith('.A'):
                section = 'author'
            elif line.startswith('.W'):
                section = 'abstract'
            elif line.startswith('.X'):
                section = 'references'
            else:
                if section == 'title':
                    current_title += line
                elif section == 'author':
                    current_author += line
                elif section == 'abstract':
                    current_abstract += line
                elif section == 'references':
                    current_references += line

        if current_doc_id is not None:
            documents[current_doc_id] = {
                "title": current_title.strip(),
                "author": current_author.strip(),
                "abstract": current_abstract.strip(),
                "references": current_references.strip()
            }


  

def write_documents(collection):
    '''
    Writes the data structure to the processed folder
    '''

    # TODO: fill in the rest
   

    output_file = './processed/' + collection + '.documents'  # Choose appropriate extension
    if os.path.exists(output_file):
        raise Exception(f"Output file {output_file} already exists.")

    with open(output_file, 'w') as file:
        for doc_id, content in documents.items():
            #content["ID"] = doc_id
            file.write(f"{doc_id}\n{content}\n\n")  # Format may vary based on requirements




if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: check for invalid parameters
    # TODO: print 'SUCCESS' to STDOUT if all went well
    if len(sys.argv) != 2:
        print("Usage: python read_corpus.py <collection_name>")
        sys.exit(1)

    collection_name = sys.argv[1]
    try:
        read_documents(collection_name)
        write_documents(collection_name)

        
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("SUCCESS")
    exit(0)