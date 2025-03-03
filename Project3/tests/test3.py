import subprocess
import sys

# Define hard-coded invalid inputs for testing
invalid_inputs = [
    ('None', 'nnn', '10', 'cycling'),  # Missing collection
    ('good', 'aaa', '10', 'cycling'),  # Wrong scoring scheme
    ('good', 'nnn', '10', ''),  # Empty query
    ('good', 'nnn', 'aaa', 'cycling'),  # Non-numeric max answers
    ('good', 'nnn', '10', 'dhjaskfhdasiogf'),  # OOV terms
]

# Function to run the test for each invalid input
def run_invalid_input_tests():
    error_detected = 0
    for i, (collection, scheme, max_answers, query) in enumerate(invalid_inputs, start=1):
        command = ['python3', './code/query.py', collection, scheme, max_answers, query]
        try:
            result = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.stdout == '':
                #print(f"Test {i} correctly failed.")
                error_detected += 1
                

            #print(f"Test {i} unexpectedly passed with output: {result.stdout}")
        except subprocess.CalledProcessError as e:
            #print(f"Test {i} correctly failed.")
            error_detected += 1
    #print(error_detected)
    return error_detected == len(invalid_inputs)

# Main function to run all tests
if __name__ == "__main__":
    all_passed = run_invalid_input_tests()

    if all_passed:
        print("PASS")
    else:
        print("FAIL")
