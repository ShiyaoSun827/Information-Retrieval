import sys
import heapq
import json
from collections import defaultdict
from preprocessing import tokenize, normalize
import math


normalization_method = 's'
def read_index(collection):
    '''
    Reads an inverted index (inside the 'processed' folder).
    '''

    queries_file = './processed/' + collection + '.json'
    try:
        with open(queries_file, 'r') as file:
            index = json.load(file)
    except FileNotFoundError:
        raise ValueError(f"Inverted index file for collection '{collection}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON from file '{queries_file}'.")
    return index

def build_query_vector(keyword_query):
    '''
    Takes a query, tokenizes and normalizes it, builds a query vector
    using the 'nnn' weighting scheme.
    '''

    global normalization_method
    # Select normalization method based on the global variable
    method = 'lemmatization' if normalization_method == 'l' else 'stemming'
    terms = normalize(tokenize(keyword_query), method=method)
    query_vector = defaultdict(int)
    for term in terms:
        query_vector[term] += 1
    return query_vector


def cosine_normalization(doc_weights):
    sum_of_squares = sum(w**2 for w in doc_weights.values())
    return 1 / math.sqrt(sum_of_squares) if sum_of_squares > 0 else 0

def tokenize_and_answer(keyword_query, tf_scheme, df_scheme, normalization, k):
    '''
    Takes a query, tokenizes and normalizes it, builds a query vector, 
    and scores the documents using the dot product algorithm discussed in class,
    returns the k highest ranked documents in order.
    '''
    assert type(keyword_query) == str
    query_vector = build_query_vector(keyword_query)
    scores = defaultdict(float)
    document_weights = defaultdict(dict)
    N = index.pop("total_documents", None)

    tf_weight = {
        'n': lambda tf: tf,
        'l': lambda tf: 1 + math.log10(tf) if tf > 0 else 0,
    }
    idf_weight = {
        'n': lambda df: 1,
        't': lambda df: math.log10(N / df) if df > 0 else 0,
    }
    normaliz = {
        'n': lambda weights, docID: 1,
        'c': lambda weights, docID: cosine_normalization(weights[docID]),
    }

    for term in index:
        df_term = index[term]['DF']
        idf = idf_weight[df_scheme](df_term)
        for doc_info in index[term]['TF']:
            docID, tf = doc_info
            tf = tf_weight[tf_scheme](tf)
            document_weights[docID][term] = tf * idf


    for term, q_weight in query_vector.items():
        if term in index:
            for doc_info in index[term]['TF']:
                docID, tf = doc_info
                weight = document_weights[docID].get(term, 0)
                norm_factor = normaliz[normalization](document_weights, docID) if normalization in normaliz else 1
                score = weight * q_weight * norm_factor 
                scores[docID] += score

    min_heap = []
    for docID, score in scores.items():
        heapq.heappush(min_heap, (score, docID))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    answer = sorted([(docID, round(score, 3)) for score, docID in min_heap], key=lambda x: (-x[1], x[0]))
    return answer
    
index = {}
if __name__ == "__main__":
    '''
    "main()" function goes here
    '''

    if len(sys.argv) < 6:
        print("Usage: python ./code/query.py <collection_name> <scoring_scheme> <normalization> <k> <keyword_query>")
        sys.exit(1)
    
    collection_name = sys.argv[1]
    scoring_scheme = sys.argv[2]
 
    normalization_method = sys.argv[3]
    k = int(sys.argv[4])
    keyword_query = ' '.join(sys.argv[5:])
    if normalization_method == 'l':
        collection_name += "_lemmatized_index"
    elif normalization_method == 's':
        collection_name += "_stemmed_index"
    else:
        print("Invalid normalization method. Only 'l' or 's' can be accepted")
        sys.exit(1)
    try:
        tf_scheme, df_scheme, normalization = scoring_scheme
        index = read_index(collection_name)
        answers = tokenize_and_answer(keyword_query, tf_scheme, df_scheme, normalization, k)
        for docID, score in sorted(answers, key=lambda x: (-x[1], x[0])):
            print(f"{docID}:{score}", end='\t')
    except ValueError as e:
        print(e)
        sys.exit(1)
