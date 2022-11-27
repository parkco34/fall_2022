#!/usr/bin/env python
# Cory Parker
# CPT101 => PIG
from random import randint
"""
Pig is a game that has two players (in our case one human and one computer) that alternate turns.  
Each player’s goal is to get 100 points rolled on a normal six-sided die first.  
Each turn consists of the rolling the die repeatedly until you get a 1 or decide to stop.  
As long as you roll a 2-6, you will add this amount to your total for that turn.  
But if you roll a 1 during your turn, your turn ends and you receive zero points for that entire turn (erasing all of the progress you made since you last agreed to stop).  
If you decide to stop rolling at any point in your turn, your points for that turn are then added to the overall score.  
The overall score is then safe from future rolls.  
The trick is knowing how long to push it before we should stop and save our gains. See end of this document for an example of a game of pig
------------------------------------------------------------------------------------------------------------------------
Structure Plan:
1) Create Die, using random module for the dice rolls
2) Create Players (human and computer), alternating turns with each die roll
3) If die roll returns a number between 2 and 6, then add to current amount.
Else if die roll returns a 1, player's amount goes to zero. But if player
decides to quit the turn, player keeps amount until his next turn.
First one to 100 wins.
------------------------------------------------------------------------------------------------------------------------
"""
die = randint(1, 6)

def player(num=0):
    """
    Input of a 1 or 0 will determine who goes first, where the human player
    goes first by default, returning the name of the player who wins.
    """
    if num % 2 == 0:
        player = input("Please enter your name: \n")
        return player

    else:
        return "Computer"


def pig(player):
    amount= 0
    quit = False
    while quit != "q":
        die = randint(1, 6)
        amount += die
        print(amount)
        quit = input("\nWanna stop here? (Type 'q' if so)\n")

        if quit == "q":
            break

        elif amount >= 20:
            return f"{player} Wins!"


if __name__ == "__main__":
    pig(player())
