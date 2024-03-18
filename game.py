##OPS445 Group Project
##Student Name: Rina An
##Student Number:102664224

import random

while True:

    options = ["rock", "paper", "scissors"] #list of options for the computer

    user_option = input("Enter your option (rock, paper, or scissors): ").lower()
    computerOption = random.choice(options) #This will choose a random option from the list for the computer

    print(f"\nYou chose {user_option}, computer chose {computerOption}.\n")

    if (user_option == "rock" and computerOption == "scissors") or \
         (user_option == "paper" and computerOption == "rock") or \
         (user_option == "scissors" and computerOption == "paper"):
        print("You won the game!")
    elif user_option == computerOption:
        print("This game is a tie!")
    else:
        print("Computer won the game!")

    play_again = input("Continue the game? (yes/no): ")
    if play_again != 'yes':
        print("Exit the game")
        break