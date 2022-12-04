# https://adventofcode.com/2022/day/3
input = [l.strip() for l in open("src/day3/input.txt")]
newList = []
bothCompartments = 0
badge = 0
def isLowerOrNah(char):
    return (ord(char) - ord("a") + 1 ) if char.islower() else (ord(char) - ord("A") + 27)

# task 1
for item in input:
    found = False
    compartment1,compartment2 = item[:len(item)//2], item[len(item)//2: len(item)]
    for char1 in compartment1:
        if(found):
            break
        for char2 in compartment2:
            if(char1 == char2):
                bothCompartments += isLowerOrNah(char1)
                found = True
                break
                # print( isLowerOrNah(char2))

# task 2
for i in range(0, len(input), 3):
    found = False
    elf1, elf2, elf3 = input[i],input[i+1],input[i+2]
    for char in elf1:
        if char in elf2 and char in elf3:
            badge += isLowerOrNah(char)
            break


print(bothCompartments)
print(badge)