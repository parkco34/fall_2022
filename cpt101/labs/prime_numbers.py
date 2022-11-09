#!/usr/bin/env python
# Cory Parker
# CPT101  
# Prime Numbers

""""
Write a boolean function named is_prime, which takes an integer as an argument
and returns true if the argument is a prime number, or false otherwise.
Use a function in the program that prompts a user to enter a number then
displays a message indicating whether the number is prime.
"""

def is_prime(num):
    # Loop through every number up to the one given
    for i in range(2, num):
        # If it's divisble by any number up to the one give, False
        if num % i == 0:
            return False

    # Otherwise, it must be PRIME!
    return True


num = int(input("\nEnter a number plz:\n"))

if __name__ == "__main__":
    print(is_prime(num))
