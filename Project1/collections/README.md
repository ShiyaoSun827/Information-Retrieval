
# Important 

**Do not write documentation here -- TAs will not read this file during grading.**

# What is this folder for?

You must keep all **input test collection files** here, including the ones you create. 

Each test collection must have three files, with extensions `.ALL`, `QRY`, and `REL`. The format of each file is described below.

# About the CISI test collection

This test collection was published with Kaggle: https://www.kaggle.com/datasets/dmaso01dsta/cisi-a-dataset-for-information-retrieval

The authors describe their test collection as:

> The data were collected by the Centre for Inventions and Scientific Information ("CISI") and consist of text data about 1,460 documents and 112 associated queries. Its purpose is to be used to build models of information retrieval where a given query will return a list of document IDs relevant to the query. The file "CISI.REL" contains the correct list (ie. "gold standard" or "ground proof") of query-document matching and your model can be compared against this "gold standard" to see how it has performed.

### CISI.ALL

This file contains the documents. 

> A file of 1,460 "documents" each with a unique ID (.I), title (.T), author (.A), abstract (.W) and list of cross-references to other documents (.X). It is the dataset for training IR models when used in conjunction with the Queries (CISI.QRY).

### CISI.QRY

This file contains the queries.

> A file containing 112 queries each with a unique ID (.I) and query text (.W).

### CISI.REL

This file contains a mapping of query IDs to IDs of relevant documents. 

> A file containing the mapping of query ID (column 0) to document ID (column 1). A query may map to more than one document ID. This file contains the "ground truth" that links queries to documents. Use this to train and test your algorithm.

*NOTE*: the two last columns have only zeroes. They can be ignored for the assignments in CMPUT361.


### Checksums

```
MD5 (data/CISI.ALL) = 791c230602e9750732802dc800e88049
MD5 (data/CISI.REL) = f57efb3ebe0f06102d69fe09f75d7a70
MD5 (data/CISI.QRY) = 378ff90778e1ff3e9fa1be26ecef0cfc
```

https://www.google.com/search?q=how+do+i+check+md5+checksum+command+line

