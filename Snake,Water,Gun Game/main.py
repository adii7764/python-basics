'''
1 for snake
-1 for water
0 for gun'''
import random

# 1 for snake, -1 for water, 0 for gun
computer = random.choice([1, -1, 0])

you = input("Enter your choice (s for snake, w for water, g for gun): ")
youDict = {"s": 1, "w": -1, "g": 0}

younum = youDict[you]

print(f"Computer chose: {computer}")
print(f"You chose: {younum}")

if computer == younum:
    print("It's a draw!")

elif (computer == -1 and younum == 1):
    print("You win!")

elif (computer == -1 and younum == 0):
    print("You lose!")

elif (computer == 1 and younum == -1):
    print("You lose!")

elif (computer == 1 and younum == 0):
    print("You win!")

elif (computer == 0 and younum == -1):
    print("You win!")

elif (computer == 0 and younum == 1):
    print("You lose!")