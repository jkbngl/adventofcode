filename = './input.txt'

with open(filename) as file:
    lines = [line.rstrip() for line in file]

firstlist = [] 
secondlist = [] 

for line in lines:
    firstlist.append(int(line.split('   ')[0]))
    secondlist.append(int(line.split('   ')[1]))

firstlist.sort()
secondlist.sort()

distances = 0

for i in range(len(firstlist)):
    distance = abs((secondlist[i] - firstlist[i]))
    print(distance)
    distances += distance

print(distances)