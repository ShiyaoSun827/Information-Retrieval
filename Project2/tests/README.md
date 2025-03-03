# Important

Document your test cases following the convention below.

# test1.py

**Purpose:** test if `build_matrix.py` on `good` collection produces the correct matrix by comparing against a hard-coded matrix.

**Expected output:** PASS

**Example run**:

```bash
% python3 tests/test1.py
Testing if matrix is built correctly -- expected to PASS
PASS
```

# test2.py

**Purpose:** test if `query.py` on `good` collection produces the correct answer for each query.

**Expected output:** PASS

**Example run**:

```bash
% python3 tests/test2.py
Testing if the output of query on `good` collection are correctly -- expected to PASS
PASS
```

# test3.py

**Purpose:** Testing five times if the query.py on `good` collection gives FAIL when it receive an invalid query expression

**Expected output:** FAIL

**Example run**:

```bash
% python3 tests/test3.py
Testing if the output of query on `good` collection gives FAIL when query.py receive an invalid query expression -- expected to FAIL
FAIL
```

# test4.py

**Purpose:** test if `query.py` on `CISI_bool` collection produces the correct answer for each query.

**Expected output:** PASS

**Example run**:

```bash
% python3 tests/test4.py
Testing if the output of query on `CISI_bool` collection are correctly -- expected to PASS
PASS
```
...
