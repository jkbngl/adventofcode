import math

filename = './input_example.txt'
# filename = './input_example_easy.txt'
# filename = './input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

rules = [l for l in lines if '|' in l]
pages = [l for l in lines if ',' in l]

# Convert to map to easier query
rules = {rules[i]: rules[i] for i in range(len(rules))}

for j, page in enumerate(pages):
    pairs = page.split(',')

    print(f"Sorting: {pairs}")

    for i, pair in enumerate(pairs):
        # print("Checking pair at index ", i)
        # Last one not compared
        if i == len(pairs) - 1:
            break

        firstnum = pairs[i]
        secondnum = pairs[i+1]

        ruleA = rules.get(f"{firstnum}|{secondnum}")
        ruleB = rules.get(f"{secondnum}|{firstnum}")

        rule = ruleA if ruleA else ruleB

        if rule:
            print(f"Comparing {firstnum} with {secondnum} -> {rule}")

            firstrule = rule.split('|')[0]
            secondrule = rule.split('|')[1]

            if firstnum != firstrule:
                print(f"-> Swapping {firstnum} with {firstrule}")
                pairs[i], pairs[i+1] = pairs[i+1], pairs[i]
                print(f"-> New page: {pairs}")
            else:
                print(f"{firstnum} and {secondnum} have no rule")
                pass
        
        print("+++++")
        # Recheck the same after switch
        firstnum = pairs[i]
        secondnum = pairs[i+1]

        ruleA = rules.get(f"{firstnum}|{secondnum}")
        ruleB = rules.get(f"{secondnum}|{firstnum}")

        rule = ruleA if ruleA else ruleB

        if rule:
            print(f"Comparing {firstnum} with {secondnum} -> {rule}")

            firstrule = rule.split('|')[0]
            secondrule = rule.split('|')[1]

            if firstnum != firstrule:
                print(f"Swapping {firstnum} with {firstrule}")
                pairs[i], pairs[i+1] = pairs[i+1], pairs[i]
            else:
                print(f"{firstnum} and {secondnum} have no rule")
                pass
                
    print("Sorted: ", pairs)
    print("-------------------")
    pages[j] = pairs

res = 0
# print('##############')
# for page in pages:
#     res += int(page[math.floor(len(page)/2)])
#     print(f"Page: {page} -> {page[math.floor(len(page)/2)]}")


# print(f"Result: {res}")


# 10890 your answer is too high
