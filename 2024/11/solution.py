import math

# filename = './input_example2.txt'
# filename = './input_example.txt'
filename = './input.txt'

with open(filename) as file:
    nums = file.read()

nums = nums.split(' ')

print(f"Initial Nums: {nums}")

i = 0
while i < 75:
    new_nums = []
    for num in nums:
        if int(num) == 0:
            new_nums.append(1)
        elif len(str(num)) % 2 == 0:

            str_num = str(num)
            half_digits = int((len(str_num)/2))

            new_nums.append(int(str_num[:half_digits]))
            new_nums.append(int(str_num[half_digits:]))
        else:

            new_nums.append((int(num) * 2024))
    
    nums = new_nums

    # print(f"{i} - Nums: {nums}")
    print(f"{i} - {len(nums)}")

    i += 1

print(f"Final nums: {len(nums)}")


# 186464 too low
# 283912 too high
