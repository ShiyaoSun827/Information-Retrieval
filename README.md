# Advanced Information Retrieval System

## Overview: Efficient Document Retrieval, Ranking, and Query Processing

This project implements a **high-performance Information Retrieval (IR) system**, designed to process and manage large-scale text collections efficiently. It integrates advanced **Natural Language Processing (NLP) techniques**, **Boolean and ranked retrieval models**, **statistical ranking methods**, **clustering**, and **classification techniques**, making it a powerful tool for structured text searching and retrieval.

## Key Technologies and Techniques

### 1. Natural Language Processing (NLP)
- **Tokenization and Normalization**: Convert text into tokens using **NLTK-based techniques**, including **case folding, stemming, and lemmatization**.
- **TF-IDF Scoring and Cosine Similarity**: Utilize **Term Frequency-Inverse Document Frequency (TF-IDF)** weighting and **cosine similarity** for ranking.
- **Probabilistic Language Models (PLM)**: Implement **Bayesian probability models** for text classification and ranking.
- **Levenshtein Distance for Approximate Matching**: Enhance recall through fuzzy search techniques.
- **Porter Stemming Algorithm & WordNet Lemmatization**: Normalize words to their root forms to improve query matching.
- **Query Expansion using Thesaurus & Relevance Feedback**: Improve recall by expanding queries with synonymous terms.
- **Soundex and Phonetic Algorithms**: Improve retrieval accuracy by accounting for phonetic variations in queries.

### 2. Indexing and Query Processing
- **Inverted Indexing**: Store term occurrences using an optimized **inverted index** to enable rapid query execution.
- **Boolean Query Processing**: Support logical operations such as **AND, OR, and NOT**.
- **Vector Space Model (VSM)**: Represent documents as numerical vectors in multi-dimensional space for similarity-based ranking.
- **Dot-Product Scoring**: Compute **document-query similarity** using the **dot product of term weight vectors**.
- **Heap-Based Ranking**: Utilize a **min heap** to efficiently retrieve the top-k highest-ranked documents.
- **Normalization Strategies**: Implement **tf-idf (ltn)** weighting schemes and **cosine normalization** to standardize document scores.
- **Zone-Based Indexing & Metadata Filtering**: Index structured fields like titles, abstracts, and body separately for enhanced ranking.
- **Web Crawling and Indexing**: Implement **distributed crawling**, **duplicate detection**, and **robot exclusion rule compliance** to build large-scale search engines.
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
- **Grid Search and Randomized Search for Parameter Tuning**: Optimize search effectiveness using **systematic hyperparameter tuning**.

## References
- [Information Retrieval - Wikipedia](https://en.wikipedia.org/wiki/Information_retrieval)
- [NLTK - Natural Language Toolkit](https://www.nltk.org/)
- [Stanford IR Book - Text Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval.html)
- [TF-IDF Scoring](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Mean Reciprocal Rank (MRR)](https://en.wikipedia.org/wiki/Mean_reciprocal_rank)
- [Mean Average Precision (MAP)](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval))
- [PageRank Algorithm](https://en.wikipedia.org/wiki/PageRank)
- [K-Means Clustering - Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)
- [Naïve Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)

This project demonstrates expertise in **Natural Language Processing (NLP), TF-IDF scoring, Boolean retrieval, probabilistic ranking, dot-product similarity computation, classification (Naïve Bayes, KNN, Rocchio), clustering (K-Means), web crawling, duplicate detection, PageRank, and query expansion**, ensuring scalable and high-performance search capabilities.

