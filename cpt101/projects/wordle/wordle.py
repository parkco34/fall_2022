#!/usr/bin/env python
# Cory Parker
# CPT101
# Wordle
"""
Computer picks a 5-letter word and keeps it hidden.
User guesses a 5-letter word and is informed:
    - Letters in the word and their positions
    - Letters in the word, but in the wrong positions
    - Letters not in the word at all
- All guesses must be valid words
- User gets 6 guesses 
GREEN - Correct letter in correct position
ORANGE - Correct letter in incorrect position
BLACK - Incorrect letter in incorrect position
------------------------------------------------------
PLAN:
    - Read file of words: word_list.txt and determine difficulty
    - Computer selects the word
    - User guesses w/ conditions
    - Position and correct, incorrect letters outputted, and color-coded
    - Fancy display everything...
"""
from random import choice

def generate_word(difficulty):
    # Picks random word from word_list.txt
    file = open("word_list.txt", "r")
    word_list = file.read().split() # List of words... duh
    return choice(word_list)

def user_guess():
    # Gets the user input for the guesses
    return input("Guess: \n")

def wordle():
    # Determines which letters are correct/incorrect along with positions
    pass

def main():
    pass

if __name__ == "__main__":
    main()

