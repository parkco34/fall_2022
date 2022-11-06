#!/usr/bin/env python

"""
Cory Parker
Lab2: Ingredient Adjuster
_________________________________________________
Recipe that asks the user how many cookies they'd like to bake, with the
appropriate amount if ingredients.
It then displays the number of cups of each ingredient needed for the given
number of cookies

Ingredients: 
    1.5 cups of sugar
    1 cup of butter
    2.75 cups of flour
5.25 cups of ingredients for 48 cookies
"""

num_cookies = int(input("Enter the number of cookies you'd like to bake: \n"))
# Constants
SUGAR = 1.5
FLOUR = 2.75

sugar = (SUGAR* num_cookies) / 48
butter = num_cookies / 48
flour = (FLOUR * num_cookies) / 48


print(f"""
Ingredients:\n
Sugar: {sugar:.2f}\n
Butter: {butter:.2f}\n
Flour: {flour:.2f}\n
      Cookies: {num_cookies:d}\n
""")

