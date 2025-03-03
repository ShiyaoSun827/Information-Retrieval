import sys
import random
import subprocess
import os
def validate_arguments(args):
    """
    Validate the command line arguments.
    """
    if len(args) != 7:
        print("Usage: python evaluation.py <collection_name> <weighting_scheme> <text_normalization> <k> <n> <evaluation_metric>")
        sys.exit(1)
    
    try:
        k = int(args[4])
        n = int(args[5])
        if k <= 0 or n <= 0:
            raise ValueError
    except ValueError:
        print("Both <k> and <n> must be positive integers.")
        sys.exit(1)
    
    if args[3] not in ['l', 's']:
        print("<text_normalization> must be either 'l' for lemmatization or 's' for stemming.")
        sys.exit(1)
    
    if args[6] not in ['mrr', 'map']:
        print("<evaluation_metric> must be either 'mrr' for Mean Reciprocal Rank or 'map' for Mean Average Precision.")
        sys.exit(1)

queries = {}
def read_queries(collection, extension):
    queries_file = './collections/' + collection + extension
    if not os.path.exists(queries_file):
        raise FileNotFoundError(f"The file {queries_file} does not exist.")

    with open(queries_file, 'r') as file:
        query_id = ''
        query_text = ''
        found_w = True

        for line in file:
            if line.startswith('.I'):
                new_query_id = line.split()[1]
                if query_id:
                    #if not found_w:
                        
                        #raise ValueError(f"{collection + extension}: Missing required '.W' section in query {query_id}")
                    if query_id in queries:
                        raise ValueError(f"{collection + extension}: Duplicate ID {query_id}")
                    queries[query_id] = query_text.strip()
                if new_query_id in queries:
                    raise ValueError(f"{collection + extension}: Duplicate ID {new_query_id}")
                query_id = new_query_id
                query_text = ''
                #found_w = False
            elif line.startswith('.W'):
                #if found_w:
                    #raise ValueError(f"{collection + extension}: Duplicated '.W' section in query {query_id}")
                found_w = True
            else:
                if found_w:
                    query_text += line

        if query_id:
            #if not found_w:
                #raise ValueError(f"{collection + extension}: Missing required '.W' section in query {query_id}")
            if query_id in queries:
                raise ValueError(f"{collection + extension}: Duplicated ID {query_id}")
            queries[query_id] = query_text.strip()

answers = {}
def read_answers(collection, extension):

    answers_file = './collections/' + collection + extension
    if not os.path.exists(answers_file):
        raise FileNotFoundError(f"The file {answers_file} does not exist.")

    with open(answers_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 2:
                raise ValueError(f"{collection}{extension}: Missing required sections in document {line}")

            query_id, doc_id = parts[0], parts[1]
            if query_id in answers and doc_id in answers[query_id]:
                raise ValueError(f"Duplicate document ID {doc_id} found for query ID {query_id}")

            if query_id not in answers:
                answers[query_id] = []
            answers[query_id].append(doc_id)

def select_random_queries(queries, n):
    """
    Selects n random queries from the queries dictionary.
    """
    if n >= len(queries):
        return queries
    random_query_ids = random.sample(list(queries.keys()), n)
    selected_queries = {query_id: queries[query_id] for query_id in random_query_ids}
    return selected_queries

def search_query(collection_name, weighting_scheme, text_normalization, k, query_id, query_text):
    try:
        command = [
            "python3", "./code/query.py", collection_name, weighting_scheme, text_normalization, str(k), '"' + query_text + '"'
        ]
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        search_results = result.stdout.strip()
        

        returned_docs = [pair.split(":")[0] for pair in search_results.split("\t") if ":" in pair]
        return returned_docs
    except subprocess.CalledProcessError as e:
        print(f"Error running query.py for query ID {query_id}: {e}")
        sys.exit(1)

def evaluate_search_results(returned_docs, known_answers):
    relevant_ranks = []
    precision_at_k = []
    for rank, doc_id in enumerate(returned_docs, start=1):
        if doc_id in known_answers:
            relevant_ranks.append(rank)
            precision_at_k.append(len(relevant_ranks) / rank)
            
    first_relevant_rank = relevant_ranks[0] if relevant_ranks else 0
    average_precision = sum(precision_at_k) / len(precision_at_k) if precision_at_k else 0
    return first_relevant_rank, average_precision



if __name__ == "__main__":
    args = sys.argv
    validate_arguments(args)
    
    collection_name = args[1]
    weighting_scheme = args[2]
    text_normalization = args[3]
    k = int(args[4])
    n = int(args[5])
    evaluation_metric = args[6]

    try:
        read_queries(collection_name, '.QRY')
        read_answers(collection_name, '.REL')
    except:
        print("FAIL")
        sys.exit(1)

    if n > len(queries):
        print(f"Requested {n} queries, but only {len(queries)} are available.")
        sys.exit(1)
    else:
        selected_queries = select_random_queries(queries, n)
    
    mrr_ranks = []
    average_precisions = []

    for query_id, query_text in selected_queries.items():
        returned_docs = search_query(collection_name, weighting_scheme, text_normalization, k, query_id, query_text)
        known_answers = answers.get(query_id, [])
        first_relevant_rank, average_precision = evaluate_search_results(returned_docs, known_answers)

        if first_relevant_rank > 0:
            mrr_ranks.append(1 / first_relevant_rank)
        average_precisions.append(average_precision)

    if evaluation_metric == "mrr":
        mrr = sum(mrr_ranks) / n if mrr_ranks else 0
        print(f"Mean Reciprocal Rank (MRR): {mrr:.3f}")
    else:
        map_ = sum(average_precisions) / n if average_precisions else 0
        print(f"Mean Average Precision (MAP): {map_:.3f}")


