import random
while True:
 choices=["rock", "paper", "scissors"]

 computer=random.choice(choices)
 player=None

 while player not in choices:
   player = input("Enter rock, paper, or scissors: ").lower()


 if computer == player:
     print("It's a tie!")
 elif (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player == "paper"):
     print("Computer wins!")
 else:
     print("Player wins!")
 print("Computer chose:", computer)
 print("Player chose:", player)

 play_again = input("Do you want to play again? (yes/no): ").lower()

 if play_again != "yes":
        break

print("Thanks for playing!")
# This code is a simple implementation of the Rock-Paper-Scissors game. The player can play against the computer, and the game continues until the player chooses to stop.