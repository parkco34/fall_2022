#!/usr/bin/env python
# Cory Parker
# CPT101
# Pig Latin
"""
User input a sentence.
- Remove first letter, placing that letter at end of word
- Append string, "ay" to the word
"""

user = "I SLEPT MOST OF THE NIGHT"

def pig_latin(sentence):
    # Removes first letter of each word, placing it at the end of the word
    pig = []
    sentence_list = sentence.split()
    breakpoint()

    for word in sentence_list:
        letter = word[0]
        new = word[1:] + letter
        pig.append(new + "AY")

    return ' '.join(pig)

def main():
    user = input("\nEnter a sentence: \n").upper()
    piggy = pig_latin(user)
    print(piggy)


if __name__ == "__main__":
    main()

