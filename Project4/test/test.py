import subprocess
import itertools
import os
import json
# Configuration constants
ws = ['nnn', 'ltn', 'lnn', 'ntn', 'nnc', 'ltc', 'lnc', 'ntc']
norm = ['l', 's']
results_per_query_options = [10, 45, 76]
evaluation_metrics = ['map', 'mrr']
collection_name = 'CISI_simplified'

# Function to count the number of queries in the .QRY file
def count_queries_in_file(queries_file_path):
    with open(queries_file_path, 'r') as file:
        return sum(1 for line in file if line.startswith('.I'))

# Function to run the evaluation for a single configuration and parse the output
def evaluate_configuration(collection, scheme, norm, k, metric, num_queries):
    # Construct the evaluation command with correct parameters
    eval_command = [
        'python3', './code/evaluation.py', 
        collection, scheme, norm, str(k), 
        str(num_queries), metric
    ]
    print(eval_command)

    # Run the evaluation script and parse its output
    eval_result = subprocess.run(eval_command, text=True, capture_output=True)
    
    #if eval_result.returncode != 0:
        #print(f"Error running evaluation: {eval_result.stderr}")
        #return None
    
    # Parse and return the result from evaluation.py
    output_parts = eval_result.stdout.strip().split()
    print(output_parts)
    return {
        'parameters': output_parts[:-1],
        'score': output_parts[-1]
    }

# Main execution block
if __name__ == "__main__":
    queries_file_path = f'./collections/{collection_name}.QRY'
    num_available_queries = count_queries_in_file(queries_file_path)
    
    # Ensure the number of queries to test does not exceed the number available
    num_queries_to_test = min(100, num_available_queries)
    
    count = 1
    num_quires_list = []
    print("number available quries",num_available_queries)
    while count * 20 <= num_available_queries:
        
        num_quires_list.append(count*20)
        count+=1 
    num_quires_list.append(num_available_queries)
    print(num_quires_list)
    evaluation_results = []
    command_list = []
    index = 1
    for i in num_quires_list:

        # Iterate over all combinations of parameters
        for scheme, norm_type, k, metric in itertools.product(ws, norm, results_per_query_options, evaluation_metrics):
            print("command:",index,collection_name, scheme, norm_type, k, i,metric)
            
            result = evaluate_configuration(collection_name, scheme, norm_type, k, metric, i)
            index+=1
            if result:
                evaluation_results.append(result)
                command_list.append(f"command: {index} {collection_name} {scheme} {norm_type} {k} {i} {metric}")

        # Output the results to a JSON file for analysis
        with open(os.path.join('test', f'evaluation_results(n={i}).json'), 'w') as f:
            json.dump(evaluation_results, f, indent=4)
        with open(os.path.join('test', f'command(n={i}).json'), 'w') as f:
            json.dump(command_list, f, indent=4)

        command_list = []
        evaluation_results = []
    
    print(f"Evaluation complete. Results are saved in 'evaluation_results.json'")