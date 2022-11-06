#!/usr/bin/env python
# Cory Parker
# CPT101 - Project 1

"""
Ask user for an integer number of the starting population, percentage yearly
increase, and the number of years, displaying results in a table.
"""

# Population
popz = int(input("Initial number of population: \n"))
# Percentage yearly increse (Percentage)
perc_increase = float(input("\nEnter the precentage yearly increase: \n")) / 100
# years
years = int(input("\nEnter the number of years for population to live: \n"))

for year in range(1, years+1):
    print("\nYear          Population\n")
    # Population each year
    popz = (popz * perc_increase) + popz
    # Population each year
    print(f" {year} \t\t {str(round(popz, 5))}")


