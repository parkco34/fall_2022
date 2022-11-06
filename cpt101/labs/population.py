#!/usr/bin/env python
# Cory Parker
# Lab #6
# Population

"""
Predicts apprioximate size of population of organisms.
-------------------------------------------------------
1- User input obtaining the initial number of organisms,
    average daily population increase (percentage), 
    and number of days organisms will be left to mutiply
2- Loop printing results as a table, as the day and the population
-------------------------------------------------------
"""
# Organisms
orgs = int(input("Initial number of organisms: \n"))
# Average daily increse (Percentage)
avg_increase = float(input("\nEnter the average daily increase: \n")) / 100
# days
days = int(input("\nEnter the number of days for organisms to live: \n"))

for day in range(1, days+1):
    print("\nDay          Population\n")
    # Population each day    
    orgs = (orgs * avg_increase) + orgs
    # Population each day    
    print(f" {day} \t\t {str(round(orgs, 5))}")
