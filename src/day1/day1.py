# https://adventofcode.com/2022/day/1
tmp = []
with open("src/day1/input.txt", "r") as f:
    for lines in f:
        tmp.append(lines)
tmp.append('\n')
sum1= 0
help = []
for t in tmp:
    if(t != "\n"):
        sum1 = sum1 + int(t)
    elif('\n'):
        
        help.append(sum1)
        sum1=0
help.sort(reverse=True)
print(help[0] + help[1] + help[2])