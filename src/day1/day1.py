tmp = []
with open("test.txt", "r") as f:
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
f.close()