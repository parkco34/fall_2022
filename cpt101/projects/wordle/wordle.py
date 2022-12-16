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
- User gets 6 guesses , after which the correct word will be displayed

GREEN - Correct letter in correct position
ORANGE - Correct letter in incorrect position
BLACK - Incorrect letter in incorrect position
------------------------------------------------------
PLAN:
    - Read file of words: word_list.txt and determine difficulty
    - Computer selects the word
    - User guesses w/ conditions
    - Identify GOOD letters in CORRECT/INCORRECT position
        - If any of the letters are in the guess and in correct position,
        highlight GREEN
        - Elif any of the letters are in the guess but in the incorect
        position, highlight YELLOW
        - else, since none of the letters are in the guess, highlight nothing
        and get another guess...
    - If guess is INVALID, it doesn't count and the user can guess again

    - Display BOARD as a grid of 
"""
from random import choice

def generate_word(difficulty=None): # Somehow be able to adjust difficulty...
    # Picks random word from word_list.txt
    file = open("word_list.txt", "r")
    word_list = file.read().split() # List of words... duh
    return choice(word_list)

def user_guess():
    # Gets the user input for the guesses
    return input("Guess a word: \n")

def compare_words(guess, word):
    # Identifies the letters from one word that matches some in the other word
    # Returning the indices of the matching letters for the guess
    """
    INPUTS:
        guess: user guess (str)
        word: Randomly generated word

    OUTPUTS:
        Returns indices of correct letters
    """
    # ==> I currently have two separate measures I can use if I need to when
    # implementing the board with letters to be highlighted
    # Letters with the same index:
    same  = [j if j[0] == j[1] else None for i,j in enumerate(zip(word,
                                                                  guess))]
    # The indices of the letters in the list above ☝
    same_indices = [i if j[0] == j[1] else None for i,j in enumerate(zip(word,
                                                                    guess))]
    # Guess list of letters:
    guess_list = list(map(lambda x: x[1], zip(word, guess)))
    # The random word list of letters
    word_list = list(map(lambda x: x[0], zip(word, guess)))
    # List of common elements between the rwo word-lists:
    differences = list(set(guess_list).intersection(word_list))

def wordle():
    pass

def main():
    guess = user_guess()
    word = generate_word()
    compare_words(word, guess)

if __name__ == "__main__":
    main()

