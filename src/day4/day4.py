# https://adventofcode.com/2022/day/4
input = [l.strip() for l in open("src/day4/input.txt")]
answer1 = 0
answer2 = 0

for line in input:
    left, right = line.split(",")
    start1, end1 = left.split("-")
    start2, end2 = right.split("-")
    (start1, end1, start2, end2) = [int(x) for x in [start1, end1, start2, end2]]
    # print(start1, end1, start2, end2)
    # task 1
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        answer1 += 1
    # task 2
    if (start1 <= start2 <= end1) or (start1 <= end2 <= end1) or (start2 <= start1 <= end2) or (start2 <= end1 <= end2):
        answer2 += 1
print(answer1)
print(answer2)