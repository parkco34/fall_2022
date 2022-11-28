#!/usr/bin/env python
# Cory Parker
# CPT101-Project2
# INspired by: https://betterprogramming.pub/interview-questions-write-yahtzee-in-python-72695550d84e
from random import randint
"""
Simple Yahtzee Game
Game where players take turns rolling 5 dice.
Each turn involves up to 3 rolls, after which, each player can decide to keep
some or all of the dice and roll the remaining.
After the 3 rolls, the player ends with their total score.
Best result: when all 5 die have the same number... YAHTZEE!
- Unlimited turns, where the goal is to get Yahtzee
"""

def dice_roll():
    # Rolls dice
    return randint(1, 6)

def keep_dice(die):
    # Allows user to keep wanted dice
    keep = int(input("""\nWich die you wanna keep? (Example: 1,3,6) Separated by
                     commas\n"""))
    keeps = keep.split(',')

    if keep == "":
        return die

    return [int(die) for die in keep]

def main():
    # Initialized die list
    die = [dice_roll() for di in range(1, 7)]

    while True:
        print(f"""
\nDice: {dice1}, {dice2}, {dice3}, {dice4}, {dice5}
""")
        if dice1 == dice2 and dice2 == dice3 and dice3 == dice4 and dice4 ==\
        dice5:
            print("YAHTZEE!")
            break

        for i in keep_dice(die):
            # Loop through and pop() the index of the list of die to keep into
            # another list 

