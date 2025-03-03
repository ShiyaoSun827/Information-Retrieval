# Advanced Information Retrieval System

## Overview: Efficient Document Retrieval, Ranking, and Query Processing

This project implements a **high-performance Information Retrieval (IR) system**, designed to process and manage large-scale text collections efficiently. It integrates advanced **Natural Language Processing (NLP) techniques**, **Boolean and ranked retrieval models**, **statistical ranking methods**, **clustering**, and **classification techniques**, making it a powerful tool for structured text searching and retrieval.

## Key Technologies and Techniques

### 1. Natural Language Processing (NLP)
- **Tokenization and Normalization**: Convert text into tokens using **NLTK-based techniques**, including **case folding, stemming, and lemmatization**.
- **TF-IDF Scoring and Cosine Similarity**: Utilize **Term Frequency-Inverse Document Frequency (TF-IDF)** weighting and **cosine similarity** for ranking.
- **Probabilistic Language Models (PLM)**: Implement **Bayesian probability models** for text classification and ranking.
- **Levenshtein Distance for Approximate Matching**: Enhance recall through fuzzy search techniques.
- **Porter Stemming Algorithm**: Normalize words to their root forms to improve query matching.
- **Query Expansion**: Use **thesaurus-based term substitution** and **relevance feedback** to enhance recall and search effectiveness.
- **Soundex and Phonetic Algorithms**: Improve retrieval accuracy by accounting for phonetic variations in queries.

### 2. Indexing and Query Processing
- **Inverted Indexing**: Store term occurrences using an optimized **inverted index** to enable rapid query execution.
- **Boolean Query Processing**: Support logical operations such as **AND, OR, and NOT**.
- **Vector Space Model (VSM)**: Represent documents as numerical vectors in multi-dimensional space for similarity-based ranking.
- **Dot-Product Scoring**: Compute **document-query similarity** using the **dot product of term weight vectors**.
- **Heap-Based Ranking**: Utilize a **min heap** to efficiently retrieve the top-k highest-ranked documents.
- **Normalization Strategies**: Implement **tf-idf (ltn)** weighting schemes and **cosine normalization** to standardize document scores.
- **Zone-Based Indexing**: Improve retrieval effectiveness by indexing metadata fields (e.g., title, abstract) separately from the document body.
- **Web Crawling and Indexing**: Implement **distributed crawling**, **duplicate detection**, and **robot exclusion rule compliance** to build large-scale search engines.

### 3. Classification and Clustering
- **Naïve Bayes Classification**: Implement **probabilistic text classification** to categorize documents based on learned probability distributions.
- **Vector-Based Classification (Rocchio, KNN)**: Classify documents using **centroid-based and k-nearest neighbors (KNN) models**.
- **K-Means Clustering**: Group documents into meaningful clusters based on feature similarity.
- **Anchor Text and Web-Based Ranking**: Use **hyperlinked anchor text** to enhance document retrieval effectiveness.
- **PageRank Algorithm**: Rank web documents using **link-based authority scoring**.

### 4. Evaluation and Optimization
- **Precision and Recall Metrics**: Measure retrieval effectiveness.
- **Mean Average Precision (MAP) & F1-Score**: Evaluate ranking and classification accuracy.
- **Incidence Matrix Optimization**: Reduce computational complexity and improve efficiency.
- **Relevance Feedback & Query Expansion**: Improve search accuracy by adjusting queries based on user feedback.
- **Grid Search and Randomized Search for Parameter Tuning**: Optimize search effectiveness using **systematic hyperparameter tuning**.

## Execution Instructions

### Building the Index
To process a dataset (e.g., `CISI_simplified`):
```bash
python3 ./code/build_index.py CISI_simplified
```

### Querying the System
To process a query on `CISI_simplified`:
```bash
python3 ./code/query.py CISI_simplified ltn 10 "How can actually pertinent data, as opposed to references or entire articles themselves, be retrieved automatically in response to information requests?"
```
Expected output format:
```bash
797:8.397  1399:7.794  309:7.396  445:7.36  166:7.251
```

To process a query on the `good` collection:
```bash
python3 ./code/query.py good ltn 10 "Does the gravity on the moon is lower than on the Earth?"
```
Expected output format:
```bash
1:4.194
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
- [K-Means Clustering - Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)
- [Naïve Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
- [PageRank Algorithm](https://en.wikipedia.org/wiki/PageRank)

This project demonstrates expertise in **Natural Language Processing (NLP), TF-IDF scoring, Boolean retrieval, probabilistic ranking, dot-product similarity computation, efficient document classification, clustering, and web search techniques**, ensuring scalable and high-performance search capabilities.

