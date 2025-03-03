'''

Reads answers to queries in the collection file into memory and writes
the data structure to the processed folder.

The program will be run from the root of the repository.

'''
#The column 0 is queryID,col1 This column contains the Document ID that is relevant to the Query ID in Column 0.

import sys,os

# Suggestion: keep the answers in a dictionary, using the query ID as the key
answers = {}

def read_answers(collection):
    '''
    Reads the answers in the collection (inside the 'collections' folder).
    '''
    #answers_file = './collections/' + collection + extension

    # TODO: fill in the rest and check for errors

        
    extension = '.REL'
    answers_file = './collections/' + collection + extension
    if not os.path.exists(answers_file):
        raise Exception(f"File {answers_file} does not exist.")


    with open(answers_file, 'r') as file:
        for line in file:
            query_id, doc_id = line.strip().split()[:2]  # Only consider first two columns
            if query_id in answers:
                answers[query_id].append(doc_id)
            else:
                answers[query_id] = [doc_id]
        '''
        for line in file:
            parts = line.strip().split()
            query_id = parts[0]
            doc_ids = parts[1:]
            answers[query_id] = doc_ids
        '''



def write_answers(collection):
    '''
    Writes the data structure to the processed folder
    '''

    # TODO: fill in the rest、
    
        
    output_file = './processed/' + collection + '.answers'
    if os.path.exists(output_file):
        raise Exception(f"Output file {output_file} already exists.")


    with open(output_file, 'w') as file:
        for query_id, doc_ids in answers.items():
            file.write(f"{query_id} {' '.join(doc_ids)}\n")



if __name__ == "__main__":
    '''
    main() function
    '''
    # TODO: read the collection name from command line
    # TODO: check for invalid parameters
    # TODO: print 'SUCCESS' to STDOUT if all went well
    if len(sys.argv) != 2:
        print("Usage: python read_answers.py <collection_name>")
        sys.exit(1)

    collection_name = sys.argv[1]
    try:
            
        read_answers(collection_name)
        write_answers(collection_name)

        
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("SUCCESS")

    exit(0)