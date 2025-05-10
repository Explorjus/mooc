# Write your solution here
import csv
import os

def evaluate_expression(expression: str) -> int:
    """Evaluates a simple arithmetic expression with two operands."""
    if '+' in expression:
        left, right = expression.split('+')
        return int(left) + int(right)
    elif '-' in expression:
        left, right = expression.split('-')
        return int(left) - int(right)
    return None

def filter_solutions():
    """Reads solutions.csv, validates the results, and writes them to correct.csv and incorrect.csv."""
    input_file = "solutions.csv"
    correct_file = "correct.csv"
    incorrect_file = "incorrect.csv"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
    
    correct_lines = []
    incorrect_lines = []
    
    with open(input_file, mode='r', newline='') as infile:
        reader = csv.reader(infile, delimiter=';')
        for row in reader:
            if len(row) != 3:
                continue  # Skip malformed lines
            name, problem, result = row
            try:
                correct_result = evaluate_expression(problem)
                if correct_result == int(result):
                    correct_lines.append(row)
                else:
                    incorrect_lines.append(row)
            except ValueError:
                incorrect_lines.append(row)  # Handle any parsing errors
    
    # Write the correct results to correct.csv
    with open(correct_file, mode='w', newline='') as correct_out:
        writer = csv.writer(correct_out, delimiter=';')
        writer.writerows(correct_lines)
    
    # Write the incorrect results to incorrect.csv
    with open(incorrect_file, mode='w', newline='') as incorrect_out:
        writer = csv.writer(incorrect_out, delimiter=';')
        writer.writerows(incorrect_lines)
