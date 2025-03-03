# Advanced Information Retrieval System

## Overview: Efficient Document Retrieval, Ranking, and Evaluation

This project implements a **high-performance Information Retrieval (IR) system**, designed to process and manage large-scale text collections efficiently. It integrates advanced **Natural Language Processing (NLP) techniques**, **Boolean and ranked retrieval models**, **statistical ranking methods**, and **evaluation metrics**, making it a powerful tool for structured text searching and retrieval.

## Key Technologies and Techniques

### 1. Natural Language Processing (NLP)
- **Tokenization and Normalization**: Convert text into tokens using **NLTK-based techniques**, including **case folding, stemming, and lemmatization**.
- **TF-IDF Scoring and Cosine Similarity**: Utilize **Term Frequency-Inverse Document Frequency (TF-IDF)** weighting and **cosine similarity** for ranking.
- **Probabilistic Language Models (PLM)**: Implement **Bayesian probability models** for text classification and ranking.
- **Levenshtein Distance for Approximate Matching**: Enhance recall through fuzzy search techniques.
- **Porter Stemming Algorithm & WordNet Lemmatization**: Normalize words to their root forms to improve query matching.
- **Query Expansion using Thesaurus & Relevance Feedback**: Improve recall by expanding queries with synonymous terms.
- **Normalization Techniques (L and S)**: Apply different normalization strategies to optimize scoring schemes for retrieval effectiveness.

### 2. Indexing and Query Processing
- **Inverted Indexing**: Store term occurrences using an optimized **inverted index** to enable rapid query execution.
- **Boolean Query Processing**: Support logical operations such as **AND, OR, and NOT**.
- **Vector Space Model (VSM)**: Represent documents as numerical vectors in multi-dimensional space for similarity-based ranking.
- **Zone-Based Indexing & Metadata Filtering**: Index structured fields like titles, abstracts, and body separately for enhanced ranking.
- **Heap-Based Ranking**: Utilize a **min heap** to efficiently retrieve the top-k highest-ranked documents.
- **Learning to Rank (LTR)**: Optimize document ranking using **grid search and machine learning-based scoring models**.
- **Anchor Text and Hyperlink-Based Ranking**: Improve ranking by incorporating anchor text from linked documents.
- **PageRank Algorithm**: Assign importance scores to web pages based on link structures.

### 3. Classification and Clustering
- **Naïve Bayes Classification**: Implement **probabilistic text classification** to categorize documents based on learned probability distributions.
- **Vector-Based Classification (Rocchio, KNN)**: Classify documents using **centroid-based and k-nearest neighbors (KNN) models**.
- **K-Means Clustering**: Group documents into meaningful clusters based on feature similarity.
- **Relevance Feedback using Centroid-Based Learning**: Adjust queries dynamically based on user feedback.

### 4. Evaluation and Optimization
- **Precision and Recall Metrics**: Measure retrieval effectiveness.
- **Mean Reciprocal Rank (MRR) & Mean Average Precision (MAP)**: Evaluate ranking and classification accuracy.
- **Automated Query Evaluation**: Randomly sample queries and compute evaluation metrics programmatically.
- **Near-Duplicate Detection using Jaccard Similarity & Shingling**: Remove redundant documents to improve search efficiency.
- **Optimal Scoring Scheme Selection (NTC, LTN, etc.)**: Evaluate different scoring models under various normalization strategies to identify the most effective retrieval model.

## Execution Instructions

### Building the Index
To process a dataset (e.g., `CISI_simplified`):
```bash
python3 ./code/build_index.py CISI_simplified
```

### Querying the System
To process a query using TF-IDF with stemming:
```bash
python3 ./code/query.py CISI_simplified ltn s 10 "What are the effects of information retrieval on user interaction?"
```

To process a query using TF-IDF with lemmatization:
```bash
python3 ./code/query.py CISI_simplified ltn l 10 "What are the effects of information retrieval on user interaction?"
```

### Running Evaluation
Evaluate **Mean Reciprocal Rank (MRR)** over 100 queries:
```bash
python3 ./code/evaluation.py CISI_simplified ltn l 10 100 mrr
```
Evaluate **Mean Average Precision (MAP)** over 100 queries:
```bash
python3 ./code/evaluation.py CISI_simplified ltn l 10 100 map
```

### Running Tests
Before testing, delete previous processed files (e.g., `good.json`, `CISI_simplified.json`) from the `processed` folder:
```bash
python3 ./tests/test1.py
python3 ./tests/test2.py
python3 ./tests/test3.py
python3 ./tests/test4.py
```
All expected test outputs should return **PASS**.

## References
- [Information Retrieval - Wikipedia](https://en.wikipedia.org/wiki/Information_retrieval)
- [NLTK - Natural Language Toolkit](https://www.nltk.org/)
- [Stanford IR Book - Text Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval.html)
- [TF-IDF Scoring](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Mean Reciprocal Rank (MRR)](https://en.wikipedia.org/wiki/Mean_reciprocal_rank)
- [Mean Average Precision (MAP)](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval))
- [PageRank Algorithm](https://en.wikipedia.org/wiki/PageRank)
- [K-Means Clustering - Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)

This project demonstrates expertise in **Natural Language Processing (NLP), TF-IDF scoring, Boolean retrieval, probabilistic ranking, dot-product similarity computation, classification (Naïve Bayes, KNN, Rocchio), clustering (K-Means), web crawling, duplicate detection, PageRank, and query expansion**, ensuring scalable and high-performance search capabilities.

