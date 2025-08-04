# first, we'll need the random and time module to help the computer make random choices and decisions for what hand to pick
import random
import time


# this function prints out text with a small delay giving a typing effect that will look cool during our gameplay
# kind of giving it an old school feel so to speak
def print_slow(str):
    for letter in str:
        print(letter, end="")
        time.sleep(0.05)
    print("\n")

    # this will be where the main function for our game is


def game():
    # our following choices for out game
    choices = ["rock", "paper", "scissors"]

    # we print out a welcome message and the rules of the game for anyone who may not know them
    # using out print_slow() from earlier
    print_slow("Welcome to Rock, Paper, Scissors!")
    print_slow("The rules are simple: \nRock crushes Scissors, Scissors cuts Paper, and Paper covers Rock! ")
    print_slow("Let's start the game...")

    # the game will now continue in a loop from this point forward till the player decides they don't want to play
    while True:
        print_slow("Please enter your choice (rock/paper/scissors): ")
        player_choice = input().lower()

        # we check if the user's choice is valid and in out list of choices from earlier
        if player_choice not in choices:
            print_slow("Invalid choice. Please try again.")
            continue

        print_slow(f"You chose {player_choice}. Now it's my turn...")
        time.sleep(1)

        # the computer will now make a random choice of this round
        computer_choice = random.choice(choices)
        print_slow(f"I chose {computer_choice}.")

        # we now determine the winner of this round
        if player_choice == computer_choice:
            print_slow("It's a tie!")
        elif player_choice == "rock" and computer_choice == "scissors" or \
                player_choice == "scissors" and computer_choice == "paper" or \
                player_choice == "paper" and computer_choice == "rock":
            print_slow("You win!")
        else:
            print_slow("I win!")

        # we now ask whether the user wants to play again
        print_slow("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != "yes":
            break


# we now implement the final portion of out game which is the game function that will run when the script is executed
if __name__ == "__main__":
    game()