
# Important 

**Do not write documentation here -- TAs will not read this file during grading.**

# What is this folder for?

You must keep all **input test collection files** here, including the ones you create. 

Each test collection must have three files, with extensions `.ALL`, `QRY`, and `REL`. The format of each file is described below.

### Fields in the `.ALL` and `.QRY` files

| Field | Meaning | Required? | Can be repeated? | 
|---|---|---|---|
| ID (`.I`) | Document/Query **identifier** | Yes | No |
| Content (`.W`) | Document or query text | Yes | No |
| Title (`.T`) | Title of document/query | No | No |
| Author (`.A`) | Author of the document/ query | No | Yes |
| Bibliography (`.B`) | Citation (or part of) | No | No |
| References (`.X`) | Links across Documents | No | No |

**NOTES**:
- A line with `.I` provides an identifier for a new document or query. Identifiers must be unique within the collection.
   - All other fields are used to describe the document or query with that ID.
   - The other fields must be associated with an ID and cannot appear "on their own".
- `.I` is often followed by the ID on the same line. 
   - Other fields may appear alone in a line of the file -- meaning that the value is the line(s) that follow, until the next field indicator.
- `.X` has multiple tab-separated values (one per line), with references between documents. Its exact semantics are unknown and the field can be safely ignored.
- Most documents have all fields listed above. Some queries have only the required fields.

### The `.REL` file

This is a `TSV` file with four columns and no fields.

| Column | Meaning | Meaning | Constraints |
|---|---|---|---|
| 1st | Query ID | Unique ID | Must correspond to a query in `.QRY` |
| 2nd | Document ID |ID of a relevant document | Must correspond to a document in `.ALL`|
| 3rd | Unknown | Unknown | N/A |
| 4th | Unknown | Unknown | N/A |

You can safely ignore the last two columns in the `.REL` file.

# The `CISI_bool` collection

For the purposes of this assignment, we will only the documents from the original CISI collection will be used (see description below). The (Boolean) queries and the answers were created by the CMPUT361 instructors. 

To avoid confusion, we are using a different collection name: `CISI_bool`. 


## Original documentation about the CISI collection

The documentation below is from the authors, as described by them on Kaggle: https://www.kaggle.com/datasets/dmaso01dsta/cisi-a-dataset-for-information-retrieval

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


# Checksums

```
MD5 (CISI_bool.ALL) = 18c0cf2796ea36619d2392a1928dfe9c
MD5 (CISI_bool.QRY) = b5237651d91c73f519ee39daee4b056e
MD5 (CISI_bool.REL) = b630cf20838cf922491d1f8674295d14
```

https://www.google.com/search?q=how+do+i+check+md5+checksum+command+line

