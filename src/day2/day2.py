# https://adventofcode.com/2022/day/2
input = [l.strip() for l in open("src/day2/input.txt")]
# task 1
playerScore1 = 0
for item in input:
    pc,me = item.split()
    playerScore1 += {'X':1, "Y":2, "Z":3}[me]
    playerScore1 += {("A", "X"):3, ("A", "Y"):6, ("A", "Z"):0,
                    ("B", "X"):0, ("B", "Y"):3, ("B", "Z"):6,
                    ("C", "X"):6, ("C", "Y"):0, ("C", "Z"):3,
                    }[(pc, me)]
# task2
playerScore2 = 0
for item in input:
    pc,me = item.split()
    playerScore2 += {'X':0, "Y":3, "Z":6}[me]
    playerScore2 += {("A", "X"):3, ("A", "Y"):1, ("A", "Z"):2,
                    ("B", "X"):1, ("B", "Y"):2, ("B", "Z"):3,
                    ("C", "X"):2, ("C", "Y"):3, ("C", "Z"):1,
                    }[(pc, me)]
print(playerScore1)
print(playerScore2)
