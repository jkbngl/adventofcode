from itertools import product
import re
# filename = './input_example.txt'
filename = './input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

def print_map(map):
    for i, line in enumerate(map):
        # format the i to always be 3 characters wide
        print(f"{str(i+1).format('3')} {''.join(line)}")
    
y = 0


map = [list(row) for row in lines]

positions = 1

try:
    while y < len(map):

        x = 0
        while x < len(map[y]):

            if map[y][x] in ['^', 'v', '>', '<']:
                # print(f'Found at x: {x} y: {y}')
                if map[y][x] == '^':
                    if map[y-1][x] == '#':
                        map[y][x] = '>'
                    else:
                        map[y-1][x] = '^'
                        # mark as touched
                        map[y][x] = 'X'
                        positions += 1
                elif map[y][x] == 'v':
                    if map[y+1][x] == '#':
                        map[y][x] = '<'
                    else:
                        map[y+1][x] = 'v'
                        # mark as touched
                        map[y][x] = 'X'
                        positions += 1
                elif map[y][x] == '>':
                    if map[y][x+1] == '#':
                        map[y][x] = 'v'
                    else:
                        map[y][x+1] = '>'
                        # mark as touched
                        map[y][x] = 'X'
                        positions += 1
                elif map[y][x] == '<':
                    if map[y][x-1] == '#':
                        map[y][x] = '^'
                    else:
                        map[y][x-1] = '<'
                        # mark as touched
                        map[y][x] = 'X'
                        positions += 1
                
                # on found reset
                y = 0
                x = 0

            x += 1
        y += 1
except IndexError:
    # last one is not longer set so has to be done manually
    positions += 1
    print_map(map)

    count = sum(row.count('X') for row in map)


    print("positions: ", positions)
    print("distinct positions: ", count)


# 5481 too high
# 831 too low