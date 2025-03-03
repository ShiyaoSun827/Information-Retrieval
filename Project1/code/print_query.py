'''

Prints the *contents* of a query, as in the collection file, but read from 
a processed file.

The program will be run from the root of the repository.

'''

import sys
import os

# Suggestion: keep the quries in a dictionary, using the ID as the key
queries = {}

def read_queries(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    #queries_file = './processed/' + collection + extension

    # TODO: fill in the rest
    
        
    extension = '.queries'  # Assuming the processed files have a .txt extension
    queries_file = './processed/' + collection + extension
    if not os.path.exists(queries_file):
        raise Exception(f"Processed file for {collection} does not exist.")
    query_id = None
    content = ""

    with open(queries_file, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            if query_id is None:
                query_id = line.strip()
            elif line.strip().isdigit():
                queries[query_id] = content.strip()
                query_id = line.strip()
                content = ""
            else:
                content += line

        # Add the last query
        if query_id is not None:
            queries[query_id] = content.strip()
        '''
    with open(queries_file, 'r') as file:
        # Example processing, adjust according to your file format
        for line in file:
            query_id, content = line.strip().split(None, 1)
            queries[query_id] = content
            '''



def retrieve_query(queryID):
    '''
    Returns a query given its id
    '''

    # TODO: check for errors
    
        
    #return queries[queryID]
    if queryID in queries:
        return queries[queryID]
    else:
        return "Query not found."



if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: read query ID from command line
    # TODO: check for invalid parameters
    # TODO: print the query to STDOUT
    if len(sys.argv) != 3:
        print("Usage: python print_query.py <collection_name> <query_id>")
        sys.exit(1)
    try:
            
        collection_name = sys.argv[1]
        query_id = sys.argv[2]

        read_queries(collection_name)
        query_content = retrieve_query(query_id)

        print(query_content)
    except Exception as e:
        print(f"Error: {e}")
    
    exit(0)