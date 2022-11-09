#!/usr/bin/env python
# Cory Parker
# CPT101
# Random Guessing Game

"""
Ask for user to input a number.
If too high, display it in message and try again.
If too low, display message indicating as such and try again.
If match, then display congrats
"""
from random import randrange
# random integer from 1 to 100
da_number = randrange(1, 101)

def user_input():
    user=int(input("\nEnter a guess for what integer it could be\n"))
    # function to get guess from user
    return user

def check_guess(guess):
    guess = user_input()

    if guess == da_number:  # Guessed right!
        print("""\nᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ  !CONGRATULATIONS! ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ
              ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿)ᕗ""")
        # Returning True because maybe I wanna user this for another program or
        # something, I don't know, leave me alone
        return True

    # As long the guess isn't right, display message to user letting them know
    # if they went to high or too low, keeping track of each attempt as the
    # user enters one number after another.
    count = 0
    while guess != da_number:

        if guess < da_number:
            print("\nToo Low amigo!\n")

        else:
            print("\nToo High my guy!\n")
    
        guess = user_input()    # Get user input again


if __name__ == "__main__":
    check_guess(user_input())
