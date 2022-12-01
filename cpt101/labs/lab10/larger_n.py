#!/usr/bin/env python
# Cory Parker
# CPT101
# Larger than n
"""
Program accepts a list and a number, where we assume the list contains numbers.
Displays all the numbers in the list, greater than the number.

In main:
    - Display original list, the value, and the returned list from the get_list
    function
"""
from random import randint, sample, choice  # Import functions for randomness, 

def get_list_item(og_list, val):
    """
    Returns the list corresponding to the numbers that are larger than the
    randomly selected number
    ------------------------------
    INPUTS:
        og_list: list of integers
        val: number from which to return a list of numbers greater than val

    OUTPUTS:
        Returns a list of numbers larger than val
    ------------------------------
    """
    return [num for num in og_list if num > val]

def main():
    RAND_LIST = sample(range(1, 100), 20)   # Creates random number list
    RAND_NUM = choice(RAND_LIST)
    print(f"""
Original List: {RAND_LIST}\n
Randomly selected number: {get_list_item(RAND_LIST, RAND_NUM)}\n
Randomly Chosen Number: {RAND_NUM}\n
          """)


if __name__ == "__main__":
    main()

