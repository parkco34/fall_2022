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

def generate_word(): # Somehow be able to adjust difficulty...
    # Picks random word from word_list.txt, returns list of letters
    file = open("word_list.txt", "r")
    words_list = file.read().split() # List of words... duh
    return list(choice(words_list))

def correct_letters(guess, word):
    # Identifies correct letters in guess, returning a list of indices
    return [y for i,(x,y) in enumerate(zip(word, guess)) if x==y]

def incorrect_positions(guess, word):
    # Identifies the correct letters in the wrong positions, returning the
    # list of indces to give to the board function
    wrong_pos = []

    for indx in range(5):
        if (guess[indx] != word[indx]) and (guess[indx] in
            word):
            wrong_pos.append(guess[indx])

    return wrong_pos

def main():
    # Main game engine
    GUESSES = 6
    GAMEOVER = False
    guessed = []  # Empty list to collect already guessed words
    # Random word
    word = generate_word()

    while not GAMEOVER:
        guess = list(input("Guess the word: \n"))
        
        while ''.join(guess) in guessed or len(guess) != 5:
            if ''.join(guess) in guessed and guess != []:
                print("You've already used that word!\n")

            elif len(guess) != 5:
                print("Not a valid word\n")
            # Guess again
            guess = list(input("Guess again! \n"))

            # Add guess to guessed list
        guessed.append(''.join(guess))

        # Loop to print out guess with letters highlighted appropriately
        print("\n")
        for letter in guess:
            if letter in correct_letters(guess, word):
                print(f"\033[0;32m {letter}\033[0;0m", end=" ")

            elif letter in incorrect_positions(guess, word):
                print(f"\033[1;33m {letter}\033[0;0m", end=" ")

            else:
                print(f"{letter}", end=" ")

        print("\n")

        if guess == word or len(guessed) == GUESSES:
            GAMEOVER = True

            if guess == word:
                print(f"\n̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿\n\nYOU WIN!\n")

            elif len(guessed) == GUESSES:
                print(f"\nLo Siento...\nThe word was: {''.join(word)}")

if __name__ == "__main__":
    main()

