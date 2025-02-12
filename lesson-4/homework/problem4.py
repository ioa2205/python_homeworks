# Problem 4
import random
print("Welcome to the game!")
print("Now, we will play a game. You will generate a number between 1 and 100, I will try to guess, if it is higher, print 'Too high', if it is lower, print 'Too low', if it is between 1 and 100, print 'You guessed it right'.")
print("Let's start!")
wants_to_play = True
while wants_to_play:
    n = random.randint(1, 100)
    for i in range(10):
        guess = int(input("Enter your guess: "))
        if guess > n:
            print("Too high")
        elif guess < n:
            print("Too low")
        else:
            print("You guessed it right")
            break
        if i == 9:
            answer = input("You lost. Want to play again?").lower()
            if answer == 'y' or answer == 'yes' or answer == 'ok':
                wants_to_play = True
        else:
            wants_to_play = False
    