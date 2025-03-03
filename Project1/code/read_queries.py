'''

Reads all queries in the collection file into memory and writes
the data structure to the processed folder.

The program will be run from the root of the repository.

'''
'''
Query Identifier (".I"): This is a unique number assigned to 
each query in the collection. 
It is used to identify the query throughout the dataset.
Query Text (".W"): This section contains the actual text of the query. 
This text represents the 
information need or the question that the query is supposed to address.
.I 34 (This is the identifier for query number 34)
.W (This indicates the start of the query text)
Methods of coding used in computerized index systems. 
(This is the actual text of the query)
'''

import sys
import os

# Suggestion: keep the queries in a dictionary, using the ID as the key
queries = {}

def read_queries(collection):
    '''
    Reads the queries in the collection (inside the 'collections' folder).
    '''
    #queries_file = './collections/' + collection + extension

    # TODO: fill in the rest and check for errors
    
    extension = '.QRY'  # Extension for the queries file
    queries_file = './collections/' + collection + extension
    if not os.path.exists(queries_file):
        raise Exception(f"File {queries_file} does not exist.")

    '''
    with open(queries_file, 'r') as file:
        for line in file:
            query_id, content = line.strip().split(None, 1)
            queries[query_id] = content
    '''

    current_query_id = None
    current_content = ''
    with open(queries_file, 'r') as file:
        for line in file:
            if line.startswith('.I'):
                if current_query_id is not None:
                    queries[current_query_id] = current_content.strip()
                current_query_id = line.split()[1]
                current_content = ''
            elif line.startswith('.W'):
                continue  # Skip the '.W' line
            else:
                current_content += line

        if current_query_id is not None:
            queries[current_query_id] = current_content.strip()



def write_queries(collection):
    '''
    Writes the data structure to the processed folder
    '''

    # TODO: fill in the rest
   

    output_file = './processed/' + collection + '.queries'  # New extension for processed file
    if os.path.exists(output_file):
        raise Exception(f"Output file {output_file} already exists.")


    with open(output_file, 'w') as file:
        for query_id, content in queries.items():
            file.write(f"{query_id}\n{content}\n\n")




if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: check for invalid parameters
    # TODO: print 'SUCCESS' to STDOUT if all went well
    if len(sys.argv) != 2:
        print("Usage: python read_queries.py <collection_name>")
        sys.exit(1)

    collection_name = sys.argv[1]
    try:
        read_queries(collection_name)
        write_queries(collection_name)

        
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("SUCCESS")


    exit(0)