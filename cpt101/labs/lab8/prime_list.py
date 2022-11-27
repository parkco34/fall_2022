#!/usr/bin/env python
# Cory Parker
# cPT101
# Prime Number List

"""
Program displays all of the prime numbers from 1 to 100,
which calls the is_prime function the file prime_numbers.py
"""
def main(_range_val1, _range_val2):
    for i in range(_range_val1, _range_val2+1):
        if is_prime(i):
            print(i)

def is_prime(num):
    if num == 1:
        return False
    # Loop through every number up to the one given
    for i in range(2, num):
        # If it's divisble by any number up to the one give, False
        if num % i == 0:
            return False

    # Otherwise, it must be PRIME!
    return True

if __name__ == "__main__":
    main(int(input("\nEnter first range value:\n")), int(input(
        "\nEnter second range value:\n"
    )))
