# Bonus Problem
import random
print("Let's play a game, rock-paper-scissor\n"
"The computer randomly chooses rock, paper, or scissors using random.choice()\n"
"The player enters their choice.\n"
"Display the winner and keep track of scores for the player and the computer.\n"
"First to 5 points wins the match.")
def r_p_s():
    point = 0
    computer_point = 0
    while point < 5 and computer_point < 5:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        player_choice = input("Enter your choice:")
        if player_choice == computer_choice:
            print("No one wins, lets continue")
            continue
        if computer_choice == "rock":
            if player_choice == "paper":
                print("Oh no, you got point!")
                point += 1
            elif player_choice == "scissors":
                print("This time, I got point!!")
                computer_point += 1
        if computer_choice == "paper":
            if player_choice == "scissors":
                print("Oh no, you got point!")
                point += 1
            elif player_choice == "rock":
                print("This time, I got point!!")
                computer_point += 1
        if computer_choice == "scissors":
            if player_choice == "rock":
                print("Oh no, you got point!")
                point += 1
            elif player_choice == "paper":
                print("This time, I got point!!")
                computer_point += 1
    if computer_point >= 5:
        print("I won, you lost")
    else:
        print("No humans, you won!")

answer = input("Do you want to play a game with me?(yes/no) ").lower
if answer != "no":
    print("Ok lets begin")
    r_p_s()
else:
    print("Okk, i will play with someone else..")