#!/usr/bin/env python
# Cory Parker
# CPT101 => PIG
from random import randint
"""
Two player game where each player alternates between rolls, where for each
turn, you iteratively roll die until you get a one or stop.  If you choose to
stop, your consectutive points are  added to your current total.  If you roll
a one, zero gets added to your current total.
------------------------------------------------------------------------------------------------------------------------
"""
def die_roll(roll=True):
    # Rolls the die, returning a random integer between 1 and 6
    if not roll:
        pass    # False boolean value (None type)

    else:
        return randint(1, 6)

def computer_turn(die):
    # Deals with each Computer roll, returning the score for that turn
    if die == 1:
        return None

    else:
        return die

def user_turn(die):
    # Handes interactions with the user, returns score for that turn
    if die == 1:
        return None

    else:
        return die

def user_choice(quit):
    # Asks user if they wanna stop or keep rolling

    if quit == "q":
        return True

    else:
        return False

def victory_checker(player1, computer):
    # Input as player totals, returning the maximum
    if player1 > computer:
        return f"\nUser wins with {player1}!\nComputer has {computer}\n"

    elif player1 == computer:
        return f"\nIt's a TIE!! \nComputer: {computer} and User: {player1}\n"

    elif player1 < computer:
        return f"\nComputer wins with {computer}\nUser has {player1}\n"

def main():
    # Handles overall scores, main loop to alternate turns, winner anouncement
    # Initial values
    player1 = 0
    computer = 0
    die = die_roll()
    count = 0   # Iteration count for alternating turns
    quit = False
    
    while (player1 < 100) and (computer < 100):

        if count % 2 == 0:  # User is an even integer
            while not quit:
                if die == 1:
                    print("\nUser die is 1\n")
                    die = die_roll()
                    continue
                
                else:
                    player1 += user_turn(die)  # Add values
                    print(f"\nUser roll: {die}\nCurrent Total: {player1}\n")
                    quit = user_choice(input("\nType 'q' to stop\n"))
                    die = die_roll()    # Roll die

            count += 1

        else:
            while True:
                if die == 1:
                    die = die_roll()
                    break

                computer += computer_turn(die)   # Adds values 
                print(f"\nComputer roll:  {die}\nCurrent Total: {computer}\n")
                die = die_roll()    # Roll die

            count += 1
    
    print(f"\nWINNER: {victory_checker(player1, computer)}\n")


if __name__ == "__main__":
    main()
