import random

"""
Rules for the game:

1 for rock
-1 for paper
0 for scissor

"""


computer = random.choice ([1, -1, 0])

user_str = input("Enter your choice: ")

user_dict = {
    "rock": 1,
    "paper": -1,
    "scissor": 0
}

computer_dict = {
    1: "rock",
    -1: "paper",
    0: "scissor"
}

user = user_dict[user_str]

if user == computer:
    print("It's a tie!")

elif(user == 1 and computer == 0) or (user == -1 and computer == 1) or (user == 0 and computer == -1):
    print("You win!")

else:
    print("Computer wins! Better luck next time!")

print(f"Computer's choice: {computer_dict[computer]}")

