#!/usr/bin/env python
# Cory Parker
# CPT101
#12 Maximum of Two Values
"""
Accepts two intgers and returns the larger one.
"""

def max_value(int1, int2):
    return int1 if int1 > int2 else int2

def read_two():
    return int(input("Enter an integer value:\n"))


if __name__ == "__main__":
    print(max_value(read_two(), read_two()))
