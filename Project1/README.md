# Advanced Information Retrieval System

## Overview: Efficient Document Retrieval and Query Processing

This project implements a **high-performance Information Retrieval (IR) system**, designed to process and manage large-scale text collections efficiently. It integrates **document parsing, query handling, and relevance-based answer retrieval**, making it a powerful tool for structured text searching and retrieval.

## Implementation Details

### 1. Corpus Processing and Storage

- **Document Parsing**: Extract metadata such as document ID, title, author, abstract, and references from raw text collections.
- **Corpus Indexing**: Store processed documents in structured data formats for efficient retrieval.
- **Tokenization and Normalization**: Convert text into tokens while handling case folding, stemming, and lemmatization to improve retrieval accuracy.
- **Boolean and Ranked Retrieval Models**: Support for both Boolean IR and ranked retrieval using the **Vector Space Model (VSM)**.

### 2. Query Handling and Search Execution

- **Query Parsing**: Process structured queries from a dedicated dataset, extracting identifiers and query text.
- **Boolean Query Processing**: Implement logical operations such as AND, OR, and NOT to filter document retrieval.
- **TF-IDF Scoring and Cosine Similarity**: Rank documents based on term frequency-inverse document frequency (TF-IDF) weights and cosine similarity.
- **Probabilistic Language Model (PLM) Scoring**: Enhance ranking accuracy with probabilistic retrieval techniques.
- **Sliding Window Query Matching**: Identify relevant document sections dynamically based on context.

### 3. Answer Extraction and Ranking

- **Relevance-Based Retrieval**: Extract top-matching documents for a given query using preprocessed mappings.
- **Precision-Optimized Ranking**: Rank retrieved documents based on textual similarity and structured metadata.
- **Evaluation Metrics (Precision, Recall, F1-Score, MAP)**: Assess retrieval effectiveness using standard IR evaluation techniques.

### 4. Execution Workflow

#### Running the System

To process a dataset (e.g., `CISI`):

```bash
python3 ./code/read_corpus.py CISI
python3 ./code/read_queries.py CISI
python3 ./code/read_answers.py CISI
```

To retrieve and print specific documents, queries, and answers:

```bash
python3 ./code/print_document.py CISI 30
python3 ./code/print_query.py CISI 82
python3 ./code/print_answers.py CISI 10
```

#### Running Tests

To validate system correctness using test datasets:

**Good collection tests:**

```bash
python3 ./code/read_corpus.py good
python3 ./code/read_queries.py good
python3 ./code/read_answers.py good
python3 ./tests/testgood1.py
python3 ./tests/testgood2.py
python3 ./tests/testgood3.py  
```

**Bad collection tests:**

```bash
python3 ./code/read_corpus.py bad1
python3 ./code/read_queries.py bad1
python3 ./code/read_answers.py bad1
python3 ./tests/testbad1.py   
python3 ./tests/testbad2.py   
python3 ./tests/testbad3.py
``` 

### 5. System Optimization and Scalability

- **Dictionary-Based Storage**: Ensures fast access to processed text components.
- **Inverted Indexing**: Efficient document retrieval using term-document incidence structures.
- **Index-Based Query Lookup**: Reduces retrieval latency by using precomputed mappings.
- **Structured Data Processing**: Supports structured and unstructured document retrieval for diverse applications.

## Applications and Use Cases

- **Search Engine Development**: Core functionality for high-performance text retrieval systems.
- **Legal and Academic Research**: Efficiently extract relevant documents for case studies and literature reviews.
- **Question Answering Systems**: Enhance automated answering systems with precise document matching.
- **Data Mining and Text Analytics**: Extract insights from large textual datasets efficiently.

## References

- [Information Retrieval - Wikipedia](https://en.wikipedia.org/wiki/Information_retrieval)
- [Text Processing and Query Handling](https://nlp.stanford.edu/IR-book/information-retrieval.html)
- [Guide to Transformer Models](https://medium.com/@alejandro.itoaramendia/attention-is-all-you-need-a-complete-guide-to-transformers-8670a3f09d02)


This project showcases expertise in **high-efficiency text retrieval, document parsing, query ranking, and probabilistic IR models**, ensuring robust performance for large-scale information retrieval tasks.

