import random

number = random.randint(1,200)

n = -1
guesses = 1
while(n != number):
    n = int(input("Guess the number between 1 & 200 : "))

    if(n < number):
        print("Sorry greater number please")
        guesses += 1

    elif(n > number):
        print("Sorry lesser number please")
        guesses += 1


print(f"congratulations you've guessed the correct number which is {number} in {guesses} attempts")

