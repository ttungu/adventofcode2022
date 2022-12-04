# https://adventofcode.com/2022/day/1
allCalories = []
input = [l.strip() for l in open("src/day1/input.txt")]
for elf in ('\n'.join(input).split('\n\n')):
    sumCalories = 0
    for calorie in elf.split('\n'):
        sumCalories += int(calorie)
    allCalories.append(sumCalories)
    
allCalories.sort(reverse=True)
print(allCalories[0])
print(allCalories[0] + allCalories[1] + allCalories[2])