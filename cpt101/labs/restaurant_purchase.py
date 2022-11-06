#!/usr/bin/env python

# Restaurant Purchase
#Create a program that solves problem #8 on page 115 of your text.  Store all
#values as assigned variables or constants. Use comments at the top of your
#program to indicate your name, name of program, and short description of what
#the program in doing.  Also, comment the meaning of all variables as they are
#created. All data requests to user should be understandable (no blank lines
#                                                             expecting inputs)
#Do multiple test runs with known values to make sure it is correct before
#showing the instructor.

"""
Cory Parker
lab2: Restauarant Purchase
---------------------------------------------------------------
Calulates the total amount of a meal purchased at a restaurant, asking for user
input, where there's an 18% tip and 7% sales tax, where the total amounts are
displayed

Returns the cost, including a 18% tip and 7% sales tax
---------------------------------------------------------------
Example:
    cost = 13.95
    TIP = 0.18
    TAX = 0.07

    Returns 17.44
---------------------------------------------------------------
"""

TIP = 0.18  # Gratuity
TAX = 0.07  # Sales Tax
cost = float(input("Enter cost of meal: \n")) # Original cost of meal (float)

print(f"""\n
Cost: ${cost}\n
Tip: {TIP}\n
Tax: {TAX}\n
======================
Total: ${sum([cost, cost*TIP, cost*TAX]): .2f}\n
""")


