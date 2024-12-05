import re

# filename = './input_example.txt'
# filename = './input_example_easy.txt'
filename = './input.txt'

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

print(f"count_rows: {count_rows}")
print(f"count_column: {count_column}")

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
    column_matches += len(re.findall(pattern, ''.join(str)))
total_matches += column_matches
print(f"Column matches: {column_matches}")

diagonal_matches_rl = 0
for i in range(count_rows, -1, -1):
    str1 = ""
    str2 = ""
    for j in range(count_rows):
        try:
            val = array_3d[i+j][j]

            str1 += val
        except:
            pass

        try:
            val = array_3d[j][i+j]

            # the middle line only once, not from both sides
            if i != 0:
                str2 += val
        except:
            pass
    
    # print(f"str1: {str1} -> {len(re.findall(pattern, str1))}")
    # print(f"str2: {str2} -> {len(re.findall(pattern, str2))}")

    diagonal_matches_rl += len(re.findall(pattern, str1))
    diagonal_matches_rl += len(re.findall(pattern, str2))

print(f"Diagonal matches_rl: {diagonal_matches_rl}")

diagonal_matches_lr = 0
for i in range(count_rows):
    str1 = ""
    str2 = ""
    for j in range(count_rows):

        try:
            val = array_3d[i+j][(count_rows-1)-j]

            str1 += val
        except:
            pass

        try:
            if (i-j) >= 0:
                val = array_3d[i-j][j]

                # the middle line only once, not from both sides
                if i != (count_rows-1):
                    str2 += val
        except:
            pass


    print(f"str1: {str1} -> {len(re.findall(pattern, str1))}")
    print(f"str2: {str2} -> {len(re.findall(pattern, str2))}")

    diagonal_matches_lr += len(re.findall(pattern, str1))
    diagonal_matches_lr += len(re.findall(pattern, str2))

print(f"Diagonal matches_lr: {diagonal_matches_lr}")

total_matches += diagonal_matches_rl
total_matches += diagonal_matches_lr
print(f"Total matches: {total_matches}")


# 2316 -> That's not the right answer; your answer is too low
# 2404 -> That's not the right answer; your answer is too high
# 2397 -> That's the right answer! You are one gold star closer to saving your vacation.