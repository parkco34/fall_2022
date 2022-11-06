#!/usr/bin/env python
# Cory Parker
# Lab #6
# Average Rainfall

"""
Uses nested loops to calculate the Average Rainfall over a period of years.
The user enters a number of years, iterating through each month, obtains user
input as inches of rain fall for that month, displaying the number of months,
total inches of rainfall and the average rainfall per month for entire period.
------------------------------------------------------------------------------
1- User enters number of years
2- Loop: Loop through 12 times each year
3- User input as the rain fall in inches
4- Display:
    Number of months
    Total inches of rainfall
    Average rainfall each month for the period
------------------------------------------------------------------------------
Example_1:
    years = 1
    monthly rainfall in inches: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    
OUTPUT:
    months: 12
    Total Rain: 376.00
    Average Rainfall: 31.33

------------------------------------------------------------------------------
"""

years = input("Enter the number of years: \n")  # Years to evaluate
if not years:
    print("\nInvalid input\n")

else:
    years = int(years)  # Convert string to integer

mnths = 0   # Months set to zero for counting
total_rain = 0  # total rainfall
rain = 0    # Rainfall per month

for yr in range(years):

    for mnth in range(12):
        mnths += 1  # Month counter
        # rainfall for the month
        rain += float(input("Number of inches of rainfall for the month: \n"))

    # Total Rainfall
    total_rain += rain



print(f"\nMonths: {mnths}\n")
print(f"\nTotal Rain: {total_rain: 0.2f}\n")
print(f"\nAverage Rainfall: {total_rain / mnths: 0.2f}\n")
