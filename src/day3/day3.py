# https://adventofcode.com/2022/day/3
input = [l.strip() for l in open("src/day3/input.txt")]
newList = []
# split in half
for item in input:
    compartment1 = slice(len(item)//2)
    compartment2 = slice(len(item)//2, len(item))
    newList.append([item[compartment1], item[compartment2]])

# task1
# logic
sum = []
bothCompartments = []
found = False
for item in newList:
    found = False
    for i in range(len(item[0])):
        if(found):
            break
        for j in range(len(item[1])):
            if(item[0][i] == item[1][j]):
                bothCompartments.append(item[0][i])
                found = True
                break
# sum
result = 0
for item in bothCompartments:
    result += (ord(item)-96) if item.islower() else (ord(item)-38)
print(result)

# task2
badge = []
found = False
for i in range(0, len(input), 3):
    found = False
    for j in range(len(input[i])):
        for k in range(len(input[i+1])):
            if(found):
                break
            if(input[i][j]==input[i+1][k]):
                for l in range(len(input[i+2])):
                    if(input[i][j] == input[i+2][l]):
                        badge.append(input[i+2][l])
                        found = True
                        break

# sum
result2 = 0
for item in badge:
    result2 += (ord(item)-96) if item.islower() else (ord(item)-38)
print(result2)