import math

filename = './input_example.txt'
# filename = './input_example_easy.txt'
filename = './input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

rules = [l for l in lines if '|' in l]
pages = [l for l in lines if ',' in l]

# Convert to map to easier query
rules = {rules[i]: rules[i] for i in range(len(rules))}

for j, page in enumerate(pages):
    pairs = page.split(',')

    print(f"Sorting: {pairs}")

    # for i, pair in enumerate(pairs):
    i = 0
    while i < len(pairs):
        # print("Checking pair at index ", i)
        # Last one not compared
        # if i == len(pairs):
            # break

        firstnum = pairs[i]

        swap_done = False

        k = i
        while k < len(pairs):
            secondnum = pairs[k]

            ruleA = rules.get(f"{firstnum}|{secondnum}")
            ruleB = rules.get(f"{secondnum}|{firstnum}")

            rule = ruleA if ruleA else ruleB

            if rule:
                # print(f"Comparing {firstnum} with {secondnum} -> {rule}")

                firstrule = rule.split('|')[0]
                secondrule = rule.split('|')[1]

                if firstnum != firstrule:
                    # print(f"-> Swapping {firstnum} with {firstrule}")
                    pairs[i], pairs[k] = pairs[k], pairs[i]
                    # k = i
                    # swap_done = True

                    k += 1

                    # print(f"New pairs: {pairs}")
                else:
                    k += 1
                    # print(f"{firstnum} and {secondnum} are already in the correct order")
                    pass
            else:
                k += 1
            

            print(k)

        # if swap_done:
        #     i = 0
        # else:
        #     i += 1
        i += 1

    print("Sorted: ", pairs)
    print("-------------------")
    pages[j] = pairs

res = 0
print('##############')
for page in pages:
    res += int(page[math.floor(len(page)/2)])
    print(f"Page: {page} -> {page[math.floor(len(page)/2)]}")


print(f"Result: {res}")


# 10890 your answer is too high
# 10562 your answer is too high
