import re

filename = './input.txt'
# filename = './input_example.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

lines = ''.join(lines)

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"

# Find all matches and store them in a list
matches = re.findall(pattern, lines)

res = 0
enabled = True

for match in matches:
    if match == "do()":
        enabled = True
        print("ensabled")
    elif match == "don't()":
        enabled = False
        print("disabled")

    if match.startswith("mul(") and enabled is True:
        match = match.split(',')

        num1 = int(match[0][4:])
        num2 = int(match[1][:-1])
        print(num1)
        print(num2)
        print("-------------")

        res += (num1 * num2)
    elif match.startswith("mul(") and enabled is False:
        print(f"Skipping: {match}")
        print("-------------")

print(res)