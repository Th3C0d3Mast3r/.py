# THIS IS A BASE GAME IN PYTHON
# NOTHING FANCY-ITS JUST A BIG RANDOM MODULE USE, ALONG WITH ELSE-IF LADDER

import random

def gameFn():
    choices=["ROCK", "PAPERS", "SCISSORS"]
    computer=random.choice(choices)

    userChoice=input("ROCK, PAPERS, or SCISSORS:- ")
    if userChoice==computer:
        print("ITS THE SAME CHOICE-RETRY")
        gameFn()
    elif userChoice=="ROCK" and computer=="PAPERS":
        print("YOU LOSE")
    elif userChoice=="ROCK" and computer=="SCISSORS":
        print("YOU WIN")

    elif userChoice=="PAPER" and computer=="ROCK":
        print("YOU WIN")
    elif userChoice=="PAPER" and computer=="SCISSORS":
        print("YOU LOSE")

    elif userChoice=="SCISSORS" and computer=="ROCK":
        print("YOU LOSE")
    elif userChoice=="SCISSORS" and computer=="PAPERS":
        print("YOU WIN")
    else:
        print("WRONG INPUT")


choice=input("Wanna Play: ")
if choice=="YES":
    gameFn()
else:
    print("BYE BYE")
