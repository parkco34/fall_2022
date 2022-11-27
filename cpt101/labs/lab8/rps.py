#!/usr/bin/env python
# Cory Parker
# CPT101
# Rock, Paper, Scissors
from random import *

def computer(token):
    """
    computer's decisions, taking in a token, which is a random number between 1
    and 3, returning the corresponding choice of rock, paper, scissors
    """
    if token == 1:
        return "rock"

    elif token == 2:
        return "paper"

    elif token == 3:
        return "scissors"


def game(comp):
    """
    Game asks for user input and returns the verdict
    """
    user = input("\nRock, Paper, or Scissors?\n ")

    if user == comp:
        print(comp)
        while user == comp:
            comp = computer(randint(1, 3))
            user = input("\nRock, Paper, or Scissors?\n ").lower()
    
    # Comparing between either/or conditions
    if (comp == "rock" and user == "scissors") or (comp == "scissors" and
                                                     user == "rock"):
        print(f"Rock WINS!! \n Computer: {comp} ( ͡ʘ ͜ʖ ͡ʘ)")

    elif (comp == "scissors" and user == "paper") or (comp == "paper" and user
                                                     == "scissors"):
        print(f"Scissors WINS!! \n Computer: {comp} ( ͡ʘ ͜ʖ ͡ʘ)")

    elif (comp == "paper" and user == "rock") or (comp == "rock" and user ==
                                                  "paper"):
        print(f"Paper WINS!! \n Computer: {comp} ( ͡ʘ ͜ʖ ͡ʘ)")


if __name__ == "__main__":

    game(computer(randint(1, 3)))
