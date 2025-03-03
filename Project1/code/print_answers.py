'''

Prints the *answers* to a query, as in the collection file, but read from 
a processed file. 
Answers are document IDs and should be printed one per line.

The program will be run from the root of the repository.

'''

import sys
import os

# Suggestion: keep the answers in a dictionary, using the query ID as the key
answers = {}

def read_answers(collection):
    '''
    Reads a processed collection (inside the 'processed' folder).
    '''
    
        
    extension = '.answers'  # Assuming the processed files have a .txt extension
    answers_file = './processed/' + collection + extension
    if not os.path.exists(answers_file):
        raise Exception(f"Processed file for {collection} does not exist.")
    with open(answers_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if parts:
                query_id = parts[0]
                doc_ids = parts[1:]
                answers[query_id] = doc_ids


    


def retrieve_answers_to_query(queryID):
    '''
    Returns the answers to a query given its id
    '''

    # TODO: check for errors
    
            
    if queryID in answers:
        return answers[queryID]
    else:
        # Handle the case where the query ID is not found
        # For example, return an empty list or a suitable message
        return []

   

if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: read query ID from command line
    # TODO: check for invalid parameters
    # TODO: print the query answers to STDOUT
    # Ensure the correct number of command line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python print_answers.py <collection_name> <query_id>")
        sys.exit(1)

    #collection_name = sys.argv[1]
    #query_id = sys.argv[2]

    # Check if the query ID is a valid integer
    try:
        collection_name = sys.argv[1]
        query_id = sys.argv[2]
    except ValueError:
        print("Error: Query ID must be an integer.")
        sys.exit(1)
    try:

        # Read and process the answers
        read_answers(collection_name)
        #print(answers)
        result = retrieve_answers_to_query(query_id)
        #print(result)
        if result:
            for doc_id in result:
                print(doc_id)
        else:
            print(f"No answers found for query ID {query_id}")
    except Exception as e:
        print(f"Error: {e}")
   
    exit(0)