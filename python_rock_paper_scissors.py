import random
user_pick = input("Type ok if you are ready ")
while user_pick != "quit":
    user_pick = input("Rock, Paper or Scissors? ")
    rps_list = ["rock","paper","scissors"]
    computer_pick = random.choice(rps_list)
    print(computer_pick)
    if user_pick == "rock" and computer_pick == "rock":
        print("Draw!")
    if user_pick == "paper" and computer_pick == "paper":
        print("Draw!")
    if user_pick == "scissors" and computer_pick == "scissors":
        print("Draw!")
    if user_pick == "scissors" and computer_pick == "paper":
        print("You Win!")
    if user_pick == "rock" and computer_pick == "scissors":
        print("You Win!")
    if user_pick == "paper" and computer_pick == "rock":
        print("You Win!")
    if user_pick == "paper" and computer_pick == "scissors":
        print("You Lost!")
    if user_pick == "scissors" and computer_pick == "rock":
        print("You Lost!")
    if user_pick == "rock" and computer_pick == "paper":
        print("You Lost!")
