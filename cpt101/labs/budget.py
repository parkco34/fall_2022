#!/usr/bin/env python
# Cory Parker
# Lab 5
# Budget Analysis


"""
User inputs the target amount he/she wishes to budget for the month.
When the user enters their expenditures, the program outputs
the amount left, indicating whether they're above or below budget target.
------------------------------------------------------------------------
Inputs:
    target: (float)
    expence: (float)

Ouputs:
    Returns a float
"""
# Target variable
target = float(input("""\nEnter the amount you'd like to budget for the
                        month:\n"""))
# Difference between expense and target:
difference = target

while difference >= 0:
    expense = float(input("""
\nPlease enter your expense: (to quit, press '0') \n
                          """))

    # Decrements the target amount by each expense
    difference -= expense
    
    # If expense is 0, break out of loop
    if expense == 0.0:
        print(difference)
        break


if difference <= 0:
    print(f"\n Below Budget!! ${difference} left\n")
elif difference == target:
    print(f"\nNo money spent! ${difference} left\n")
else:
    breakpoint()
    print(f"\nWithin budget! ${difference} left\n")
