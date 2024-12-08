from itertools import product
import re
# filename = './input_example.txt'
# filename = './input_example_easy.txt'
filename = './input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

def generate_operator_combinations(n):
    operators = ['+', '*']
    # Generate all combinations of length n-1
    combinations = list(product(operators, repeat=n-1))
    return combinations

def evaluate_no_precedence(expression):
    # Split the expression into numbers and operators using regex
    tokens = re.findall(r'\d+|\+|\*', expression)
    # Convert numbers to integers
    tokens = [int(token) if token.isdigit() else token for token in tokens]
    
    # Sequentially evaluate from left to right
    result = tokens[0]
    for i in range(1, len(tokens), 2):  # Step through operators and numbers
        operator = tokens[i]
        number = tokens[i + 1]
        if operator == '+':
            result += number
        elif operator == '*':
            result *= number
    
    return result

correct_results = []
for i, line in enumerate(lines):
    continue_ = True
    
    res = line.split(':')[0]
    operators = line.split(':')[1].strip()

    combinations = generate_operator_combinations(len(operators.split(' ')))
    # print(operators)
    # print(combinations)

    for j, combination in enumerate(combinations):
        if continue_:
            combination = list(combination)
            
            operators_adj = operators

            for l, operation in enumerate(combination):
                # replace the whitespaces with the respective operator
                operators_adj = operators_adj.replace(' ', operation, 1)
            
            res_operation = evaluate_no_precedence(operators_adj)

            if res_operation == int(res):
                correct_results.append(res_operation)
                # print(f'Match: {operators_adj} = {res_operation}')
                continue_ = False


print(correct_results)
print(sum(correct_results))