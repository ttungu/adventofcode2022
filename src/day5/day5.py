# https://adventofcode.com/2022/day/5
input = [l.strip() for l in open("src/day5/input.txt")]
# remove/add from left
initialStack1 = [
    ["S", "L", "F", "Z", "D", "B", "R", "H"],
    ["R", "Z", "M", "B", "T" ],
    ["S", "N", "H", "C", "L", "Z"],
    ["J", "F", "C", "S"],
    ["B", "Z", "R", "W", "H", "G", "P" ],
    ["T", "M", "N", "D", "G", "Z", "J", "V" ],
    ["Q", "P", "S", "F", "W", "N", "L", "G" ],
    ["R", "Z", "M" ],
    ["T", "R", "V", "G", "L", "C", "M" ]
]

initialStack2 = [
    ["S", "L", "F", "Z", "D", "B", "R", "H"],
    ["R", "Z", "M", "B", "T" ],
    ["S", "N", "H", "C", "L", "Z"],
    ["J", "F", "C", "S"],
    ["B", "Z", "R", "W", "H", "G", "P" ],
    ["T", "M", "N", "D", "G", "Z", "J", "V" ],
    ["Q", "P", "S", "F", "W", "N", "L", "G" ],
    ["R", "Z", "M" ],
    ["T", "R", "V", "G", "L", "C", "M" ]
]

def getResult(stack):
    result = ""
    for crates in stack:
        result += crates[0]
    return result

# task 1
for row in input:
    string1, number, string2, where, string3, to = row.split(' ')
    # use only number, where, to
    # which translates to "move 6 from 2 to 3"
    for i in range(int(number)):
        rmeovedCrate = initialStack1[int(where)-1].pop(0)
        initialStack1[int(to)-1].insert(0, rmeovedCrate)
print(getResult(initialStack1))

# task 2
for row in input:
    string1, number, string2, where, string3, to = row.split(' ')
    number, where, to = [int(x) for x in [number, where, to]]
    if number == 1:
        rmeovedCrate = initialStack2[where-1].pop(0)
        initialStack2[to-1].insert(0, rmeovedCrate)
    else:   
        removedCrates = initialStack2[where - 1][:number]
        initialStack2[where-1] = initialStack2[where-1][number:]
        initialStack2[to-1] = removedCrates+initialStack2[to-1]

print(getResult(initialStack2))
