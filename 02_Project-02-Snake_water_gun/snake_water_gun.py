                # SNAKE , WATER AND GUN

import random 

"""
1 for snake 
-1 for water
0 for gun
"""

computer = random.choice([-1, 0, 1])
youstr = input("Enter you choice : ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer choses {reverseDict[computer]}")

if(computer == you):
    print("it's a draw , play again")

else:
    if(computer == -1 and you == 1):
        print("You win")

    elif(computer == -1 and you == 0):
        print("You lose")

    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 1 and you == -1):
        print("You lose")

    elif(computer == 0 and you == 1):
        print("You lose")

    elif(computer == 0 and you == -1):
        print("You win")

    else:
        print("something went wrong")


