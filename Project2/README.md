# Boolean Information Retrieval System

## Overview: Boolean Query Processing and Efficient Document Retrieval

This project implements a **Boolean Information Retrieval (IR) system**, enabling efficient structured queries for document retrieval. The system processes large text collections, evaluates Boolean queries using precedence rules, and ranks results using term-document incidence matrices.

## Implementation Details

### 1. Corpus Processing and Storage
- **Document Parsing**: Extract metadata and textual content from structured files.
- **Tokenization and Normalization**: Convert raw text into normalized tokens using **NLTK-based tokenization, case folding, and stemming**.
- **Boolean Query Support**: Construct a **term-document incidence matrix** for Boolean retrieval.
- **Efficient Storage**: Save processed documents and term mappings in JSON format for quick access.
- **Indexing Techniques**: Utilize **inverted index structures** to store term occurrences and enable fast query lookup.

### 2. Boolean Query Processing
- **Expression Parsing**: Implement a structured parser to handle Boolean expressions using `AND`, `OR`, and `NOT` operators.
- **Operator Precedence Handling**: Ensure correct query interpretation using **parentheses resolution and operator precedence rules**.
- **Stack-Based Query Execution**: Process queries using a stack-based evaluation method.
- **Document Matching**: Evaluate queries against the term-document matrix to return matched document IDs.

### 3. Query Execution Workflow
- **Precedence-Based Query Parsing**: Rewrite queries by applying structured **precedence handling for NOT and AND operations**.
- **Boolean Operator Evaluation**:
  - `AND`: Returns documents that contain all specified terms.
  - `OR`: Returns documents containing any of the specified terms.
  - `NOT`: Excludes documents containing the specified term.
- **Error Handling**: Detects and handles malformed expressions, missing terms, and mismatched parentheses.

### 4. Evaluation Metrics for Query Performance
- **Precision and Recall**: Measure the fraction of relevant documents retrieved and the proportion of relevant documents identified.
- **F1-Score**: A harmonic mean of precision and recall to balance retrieval effectiveness.
- **Mean Average Precision (MAP)**: Evaluate the ranking of retrieved documents.
- **Macro and Micro Averaging**: Assess retrieval performance over multiple queries.

### 5. Execution Workflow
#### Running the System
To build the term-document matrix for a collection (e.g., `CISI_bool`):
```bash
python3 ./code/build_matrix.py CISI_bool
```
To process a Boolean query:
```bash
python3 ./code/query.py CISI_bool ":not: ( t1 :and: :not: ( t2 ) )"
```
#### Running Tests
To validate system correctness using test datasets:
**Matrix Generation Tests:**
```bash
python3 ./tests/test1.py  # Validate incidence matrix correctness
```
**Query Evaluation Tests:**
```bash
python3 ./tests/test2.py  # Validate Boolean query answers
python3 ./tests/test3.py  # Validate incorrect query handling
python3 ./tests/test4.py  # Validate CISI_bool dataset query evaluation
```
### 6. System Optimization and Scalability
- **Incidence Matrix Optimization**: Uses a compact representation to improve query evaluation speed.
- **Efficient Query Execution**: Implements a stack-based algorithm for rapid Boolean evaluation.
- **Exception Handling**: Ensures robust query parsing and execution with clear error messages.
- **Levenshtein Distance for Approximate Matching**: Improve recall by allowing fuzzy matching of terms.

## Compilation/Execution Instructions
### Testing `build_matrix.py` on the `good` collection
```bash
python3 ./code/build_matrix.py good
```
### Testing `build_matrix.py` on `CISI_bool` collection
```bash
python3 ./code/build_matrix.py CISI_bool 
```
### Testing `query.py` on `good` collection
```bash
python3 ./code/query.py good ":not: ( hiking :and: reading )"
```
### Testing `query.py` on `CISI_bool` collection
```bash
python3 ./code/query.py CISI_bool "( memberships :or: sketches ) :and: :not: sociologists"
```
### Running test cases (all should pass)
```bash
python3 ./tests/test1.py
python3 ./tests/test2.py
python3 ./tests/test3.py
python3 ./tests/test4.py
```
## Applications and Use Cases
- **Legal and Compliance Search**: Enable precise document retrieval using Boolean queries.
- **Academic Research**: Retrieve relevant papers efficiently using structured keyword searches.
- **Data Mining**: Process large text corpora and extract meaningful information with Boolean logic.
- **Enterprise Search Systems**: Implement structured query-based document retrieval for large-scale datasets.

## References
- [Boolean Retrieval - Wikipedia](https://en.wikipedia.org/wiki/Boolean_retrieval)
- [Natural Language Processing - NLTK](https://www.nltk.org/)
- [Stanford IR Book - Boolean Retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html)

This project demonstrates expertise in **Boolean Information Retrieval, structured query execution, advanced indexing techniques, and efficient document ranking**, ensuring high-performance search capabilities for large-scale datasets.

