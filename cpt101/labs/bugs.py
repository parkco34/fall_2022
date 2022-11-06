#!/usr/bin/env python
# Cory Parker
# Lab 5
# Bug Collector

"""
Calculates the running total of the number of bugs collected
over the course of five days.
Iteratively asking the user for the number of bugs for each day, 
returning the total number of bugs collected.

"""

# bug counter
bugs = 0

for i in range(5):
    # Increments each daily bug collection
    bugs += int(input("""
\nEnter the number of bugs collected for the day:
    \n"""))

# Print result
print(f"""\n
Total Bugs: {bugs}
      \n""")



