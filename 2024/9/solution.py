# filename = './input_example_easy.txt'
# filename = './input_example.txt'
# filename = './input_example2.txt'
filename = './input.txt'

with open(filename) as file:
    lines = file.readlines()

lines = lines[0]

res = []
file_id = 0

for i, c in enumerate(lines):
    if i % 2 == 0:
        for j in range(int(c)):
            res.append(str(file_id))
        file_id += 1
    else:
        for j in range(int(c)):
            res.append('.')
        

print(res)

iteration = 0

while True:
    # print("--------------")
    # print(res)

    # find the first dot
    first_free = res.index(".") 
    # Last non-dot index
    last_filled = 0
    for i, c in enumerate(res):
        if c != ".":
            last_filled = i

    # print("first_free: ", first_free)
    # print("last_filled: ", last_filled)
    print(last_filled)

    if first_free > last_filled:
        break

    res[first_free] = res[last_filled]
    res[last_filled] = "."

    

    iteration += 1

print("#########")
print("FINAL RESULT")
print(res)

checksum = 0

for i, c in enumerate(res):
    if c != ".":
        checksum += i * int(c)

print(checksum)


# res -> 6331212425418 