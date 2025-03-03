'''
(1) calls build_matrix.py on your good collection; 
(2) reads the corresponding good.matrix.json file using Python’s built in JSON library; 
(3) compares the matrix read to another matrix hard-coded inside test1.py with a matrix that you create by hand out of your own good collection. The matrices must be identical.
'''

import subprocess
import sys
import json
print("Testing output of build_matrix -- expected to PASS")
matrix={
    "_M_": 5,
    "emma": [0, 1, 0, 0, 0],
    "ethan": [0, 0, 0, 0, 1],
    "jame": [0, 0, 1, 0, 0],
    "olivia": [0, 0, 0, 1, 0],
    "tv": [0, 0, 0, 1, 0],
    "tom": [1, 0, 0, 0, 0],
    "and": [1, 1, 1, 1, 1],
    "beach": [0, 0, 0, 1, 0],
    "bitter": [1, 0, 0, 1, 0],
    "but": [1, 1, 1, 1, 1],
    "classic": [0, 0, 0, 1, 0],
    "coffe": [1, 0, 0, 1, 0],
    "crowd": [1, 0, 0, 0, 1],
    "earli": [0, 1, 0, 0, 0],
    "fast": [0, 0, 0, 0, 1],
    "fiction": [1, 0, 1, 0, 0],
    "food": [1, 0, 0, 1, 1],
    "fresh": [0, 1, 0, 0, 0],
    "game": [0, 1, 1, 0, 0],
    "garden": [0, 0, 0, 0, 1],
    "hate": [1, 1, 1, 1, 1],
    "hike": [1, 0, 0, 0, 0],
    "in": [1, 0, 0, 0, 0],
    "jam": [0, 0, 1, 0, 0],
    "jazz": [0, 0, 1, 0, 0],
    "like": [1, 1, 1, 1, 1],
    "loud": [0, 1, 0, 0, 0],
    "morn": [0, 1, 0, 0, 0],
    "mountain": [1, 0, 0, 0, 0],
    "music": [0, 1, 1, 0, 0],
    "novel": [0, 0, 0, 1, 0],
    "paint": [0, 1, 0, 0, 0],
    "pastri": [0, 1, 0, 0, 0],
    "place": [1, 0, 0, 0, 1],
    "plastic": [0, 0, 1, 0, 0],
    "read": [1, 0, 1, 0, 0],
    "realiti": [0, 0, 0, 1, 0],
    "scienc": [1, 0, 1, 0, 0],
    "show": [0, 0, 0, 1, 0],
    "spici": [1, 0, 0, 1, 1],
    "sunni": [0, 0, 0, 1, 0],
    "the": [1, 0, 0, 0, 0],
    "traffic": [0, 0, 1, 0, 0],
    "video": [0, 1, 1, 0, 0],
    "wast": [0, 0, 1, 0, 0]
}
def run_read_corpus(collection_name):
    try:
        command = ['python3', './code/build_matrix.py', collection_name]  
        result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print("FAIL")
        exit(1)
    file_path = './processed/good.matrix.json'
    try:
        with open(file_path, 'r') as file:
            matrix_test = json.load(file)
    except FileNotFoundError:
        print("FAIL")
        exit(1)
    except json.JSONDecodeError:
        print("FAIL")
        exit(1)

    except Exception as e:
        print("FAIL")
        exit(1)

    if matrix == matrix_test:
        print("PASS")
        exit(0)

    else:
        print("FAIL")
        exit(1)
        
if __name__ == "__main__":
    test_collection_name = 'good' 
    run_read_corpus(test_collection_name)
    


