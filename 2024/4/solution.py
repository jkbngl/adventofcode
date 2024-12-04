import re

filename = './input_example.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

array_3d = []
for line in lines:
    # Split each section into lines, then split each line into integers
    array_2d = [l for l in line]
    array_3d.append(array_2d)

# the second and third dimension are always 0
pattern = r"(?=(XMAS|SAMX))"

# Find all matches and store them in a list
# matches = re.findall(pattern, array_3d[0][_][_])

total_matches = 0

count_rows = len(array_3d)
count_column = len(array_3d[0])

print(count_rows)

row_matches = 0
# in same row
for row in array_3d:
    row_matches += len(re.findall(pattern, ''.join(row)))
total_matches += row_matches
print(f"Row matches: {row_matches}")

column_matches = 0
# in same column
for column in range(count_column):
    str = [array_3d[row][column] for row in range(len(array_3d))]
    print(''.join(str))
    column_matches += len(re.findall(pattern, ''.join(str)))
total_matches += column_matches
print(f"Column matches: {column_matches}")

diagonal_matches_fr = 0
for i in range(9, -1, -1):
    str = ""
    for j in range(10):
        try:
            val = array_3d[i+j][j]

            str += val
            # print(f"i: {i+j}, j: {j} -> {val}")
        except:
            pass
    
    print("str: ", str)

    diagonal_matches_fr += len(re.findall(pattern, str))

print(f"Diagonal matches: {column_matches}")

total_matches += diagonal_matches_fr

diagonal_matches_rl = 0
for i in range(9, -1, -1):
    str = ""
    for j in range(10):
        try:
            val = array_3d[i+j][j]

            str += val
            # print(f"i: {i+j}, j: {j} -> {val}")
        except:
            pass
    
    print("str: ", str)

    diagonal_matches_fr += len(re.findall(pattern, str))

print(f"Diagonal matches: {column_matches}")

total_matches += diagonal_matches_fr
print(f"Total matches: {total_matches}")