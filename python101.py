# Random
import random

# WHile loop that keeps playing until you win
while True:
    # Input from user to enter their choice
    user = input("Rock, Paper, or Scissors? ").lower()
    cmptChoice = random.choice(["rock", "paper" ,"scissors"])
    print(f"The computer chose: {cmptChoice}")
    
    # Print formatting, comparison operators, & include continue and break
    if user != "rock" and user != "paper" and user != "scissors":
        print("Game Over! Try again.")
        continue
    
    if user == cmptChoice:
        print("It's a tie! Try again.")
        continue
    elif cmptChoice == "rock" and user == "paper":
        print("You win!!")
        break
    elif cmptChoice == "scissors" and user == "rock":
        print("You win!!")
        break
    elif cmptChoice == "paper" and user == "scissors":
        print("You win!!")
        break
    else:
        print("You lost! Try again :(")
        continue