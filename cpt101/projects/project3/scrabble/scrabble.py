#!/usr/bin/env python
# Cory Parker
# CPT101
# Scrabble

"""
The game of scrabble has you create words to place on a grid.  The scoring is dependent on the values of each letter in your word (along with other on-grid bonuses).  This program is going to allow the user to type in any valid English word and score the word based on the values of each of its letters.  A file with over 113,000 valid English words is provided (“Words.txt”) and this will be used to determine if the inputted word should be calculated.  If the inputted word is valid, then each character of the word will be checked for its value and the total will be reported.  The values of each of the 26 letters is listed in the provided file “ScrabbleLetterValues.txt”.  You must use this file to read in the values into your program – it is not allowed to manually create the lists in your program.
"""
def file_read(path):
    # Reads particular file in given path
    return open(path, "r").read().split()


def scorer(word):
    # Scores the scrabble; can also use previous score by entering it the
    # function manually
    array = []
    alphabet = file_read("ScrabbleLetterValues.txt")[::2]  # alphabet
    values = file_read("ScrabbleLetterValues.txt")[1::2]  # Correpsonding value

    
    for letter in word:
        array.append(  # Appends the corresponding index value
            int(values[alphabet.index(letter)])
        )

        return sum(array)

def main():
    print(f"\n{'='*30} SCRABBLE {'='*30}\n")

    user_word = input("\nEnter your word:\n").upper()
    _words = open("words.txt", "r").read().split()
    words = list(map(lambda x: x.upper(), _words))
    
    while user_word not in words:
        user_word = input("\nInvalid word:\n").upper()

    print(scorer(user_word))


if __name__ == "__main__":
    main()


