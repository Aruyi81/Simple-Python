# first we need our import statements
import random
import time

# next to the game and main meat of this program

def guess_the_number():
    number = random.randint(1, 20)
    attempts = 0

    # simple intro game statements
    print("Welcome to Guess the Number!")
    print("\n")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        guess = input("Take a guess: ")

        # input validation to see if the guess is correct type or not
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 20:
            print("Invalid guess. Please enter a number between 1 and 20.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try a higher number.")

        elif guess > number:
            print("Too high! Try a lower number.")

        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

        # create s score and leaderboard for more interactivity
        score = 100 - attempts * 5  # calculating score based on attempts
        print(f"Score: {score}")
        print("---- Leaderboard ----")
        # display leaderboard with top scores


guess_the_number()