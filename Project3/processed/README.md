# Important

# Representation of inverted index

**TODO: Document your data structure for the index here.**

Describe your data structure(s) used and how the dictionary and the postings are represented. Explain if they reside in memory or in a file while `query.py` runs.

**Our inverted index is implemented using Python dictionaries and lists. Each dictionary key is a term from the documents, and its value is a list of document IDs where the term is found. This structure facilitates efficient search and retrieval operations. The entire index, including the dictionary and postings, is held in memory during the execution of `query.py` for quick access. However, the index can be serialized to files for persistence, following specific naming conventions.**


# Naming convention 

This approach allows for the easy identification and association of index files with their respective test collections, facilitating efficient data management and querying.

- You can use as many files as you want to represent the index.
- Each file should have the same name (prior to extension) as the corresponding test collection. 
- The extensions of those files cannot be the same as in the `./collections/` folder, to avoid confusion/errors.
