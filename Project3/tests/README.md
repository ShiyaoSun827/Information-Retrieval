# Important

### TODO: Document your test cases following the convention below.

# test1.py

**Purpose:** test if `build_index.py` on your own `good` collection produces the correct index, by comparing it against a hard-coded correct index.

**Expected output:** PASS

**Example run**:

```bash
% python3 tests/test1.py
Testing if matrix is built correctly -- expected to PASS
PASS
```

# test2.py

**Purpose:** test if `query.py` on your good collection once for each of the ten queries returns the correct answer for each query

**Expected output:** PASS

**Example run**:

```bash
% python3 tests/test2.py
Testing output of query -- expected to PASS
PASS
```

# test3.py

**Purpose:** test if `query.py` can handle errors correctly, checks that program returns an error in each case.

**Expected output:** PASS

**Example run**:

```bash
% python3 tests/test3.py
PASS
```

# test4.py

**Purpose:** test if `query.py` can query correctly, checks the answer provided contains at least one document returned by  `query.py`. Choose the scoring scheme appropriately. k should be 50.

**Expected output:** PASS

**Example run**:

```bash
% python3 tests/test4.py
PASS
```
