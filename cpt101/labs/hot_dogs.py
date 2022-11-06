#!/usr/bin/env python
""""
Cory Parker
Hot Dog Cookout Calculator
------------------------------------------------------
Hot dogs come in packages of 10
Buns come in packages of 8
Calculates the number of hot dogs and bun packages are 
needed for a cookout, with the mininum amount of left overs,
depending on the number of people attending, 
and how many hot dogs per person, the user input.
=====================================================
- Min # of packages of hot dogs
- Min # of packages of hot dog buns
- # of hot dogs left over
- # of hot dog buns left over
=====================================================
------------------------------------------------------
"""

DOGS = 10
BUNS = 8
peeps = abs(int(input("\nEnter the number of people coming: \n")))
dogs = abs(int(input("\nEnter the number of hot dogs (per person):\n")))

dog_tot = peeps * dogs
pkg_dogs = dog_tot // DOGS
pkg_buns = dog_tot // BUNS

left_dogs = dog_tot % DOGS
left_buns = dog_tot % BUNS

print(
f"""
Packages of hot dogs: {pkg_dogs}\n
Packages of Buns: {pkg_buns}\n
Hot dogs left over: {left_dogs}\n
Buns left over: {left_buns}\n
"""
)
