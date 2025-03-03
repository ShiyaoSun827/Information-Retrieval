import subprocess
import sys

# Define ten different queries to be used against the CISI_simplified collection
queries = [
    "What problems and concerns are there in making up descriptive titles?What difficulties are involved in automatically retrieving articles fromapproximate titles?What is the usual relevance of the content of articles to their titles?",
    "How can actually pertinent data, as opposed to references or entire articles themselves, be retrieved automatically in response to information requests?",
    "What is information science?  Give definitions where possible.",
    "Image recognition and any other methods of automatically transforming printed text into computer-ready form.",
    "What special training will ordinary researchers and businessmen need for proper information management and unobstructed use of information retrieval systems? What problems are they likely to encounter?",
    "What possibilities are there for verbal communication between computers and humans, that is, communication via the spoken word?",
    "Describe presently working and planned systems for publishing and printing original papers by computer, and then saving the byproduct, articles coded in data-processing form, for further use in retrieval.",
    "Describe information retrieval and indexing in other languages.What bearing does it have on the science in general?",
    "What possibilities are there for automatic grammatical and contextual analysis of articles for inclusion in an information retrieval system?",
    "The use of abstract mathematics in information retrieval, e.g. group theory."
    
]
# Function to read .REL file and map queries to their relevant documents
def read_relevant_docs(rel_file):
    relevances = {}
    with open(rel_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            query_id, doc_id = parts[0], parts[1]
            if query_id in relevances:
                relevances[query_id].add(doc_id)
            else:
                relevances[query_id] = {doc_id}
    return relevances

# Modified part of run_query_test function to check the relevancy
def run_query_test(collection_name, scoring_scheme, max_results, relevances):
    passed_tests = 0
    #print(relevances.get(str(1)))

    for i, query in enumerate(queries, start=1):
        expected_docs = relevances.get(str(i))  # Change i to match your query ID format if needed
        if i == 6 :
            scoring_scheme = 'ltn'
        if i == 8 :
            scoring_scheme = 'nnc'    
        command = ['python3', './code/query.py', collection_name, scoring_scheme, str(max_results),  query ]
        #print(command)
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print(result)

        lines = result.stdout.strip().split('\t')
        #print(lines)
        result_docs = {line.split(':')[0] for line in lines if line}
        #print(result_docs)

        # Check if any of the result_docs are in the expected_docs
        if expected_docs & result_docs:  # Intersection of both sets
            #print(f"Test {i} PASSED: At least one relevant document returned.")
            passed_tests += 1
        else:
            #print(result_docs)
            print(f"Test {i} FAILED: No relevant documents were returned.")
    
    return passed_tests

if __name__ == "__main__":
    test_collection_name = 'CISI_simplified'
    scoring_scheme = 'ltc'  # Example scoring scheme; replace as needed
    max_results = 50
    rel_file = './collections/CISI_simplified.REL'  # Adjust path as necessary
    
    try:
        command_matrix = ['python3', './code/build_index.py', test_collection_name]  
        result1 = subprocess.run(command_matrix, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print("FAIL")
        sys.exit(1)
    # Read relevances from .REL file
    relevances = read_relevant_docs(rel_file)
    
    # Run the test queries and check against relevances
    total_passed_tests = run_query_test(test_collection_name, scoring_scheme, max_results, relevances)
    
    # Output the final result of the test cases
    if total_passed_tests == len(queries):
        print("PASS!")
        sys.exit(0)
    else:
        print(f"FAIL: {len(queries) - total_passed_tests} out of {len(queries)} query tests did not return a relevant document.")
        sys.exit(1)