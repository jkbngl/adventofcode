filename = './input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

unsafes = 0

for j, line in enumerate(lines):
    values = line.split(' ')
    values = list(map(int, values))

    # at the beginning both are assumed as true
    increasing_checks = 0
    decreasing_checks = 0

    for i, v in enumerate(values):
        # keep checking until the second last element
        if i < (len(values) - 1):
            # only check as long as its true
            if (values[i] < values[i+1] and (values[i] + 3) >= values[i+1]): # -> means its safely increasing
                # value is lower then the next and the value + 3 is higher as the next value, means the next value is not more then 3 higher
                increasing_checks += 1
            if (values[i] > values[i+1] and (values[i+1] + 3) >= values[i]): # -> means its safely decreasing
                # value is higher then the next and the next value + 3 is higher as the value
                decreasing_checks += 1
            
    if increasing_checks == (len(values) - 1):
        print(f"Found safe increasing pair: {values}")
    elif decreasing_checks == (len(values) - 1):
        print(f"Found safe decreasing pair: {values}")
    else:
        print(f"Found unsafe pair: {values} - increasing: {increasing_checks} decreasing {decreasing_checks}" )
        unsafes += 1

print(f"unsafes: {unsafes}")
print(f"safes: {len(lines) - unsafes}")
print(f"total: {len(lines)}")
