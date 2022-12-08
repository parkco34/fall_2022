#!/usr/bin/env python
# Cory Parker
# CPT101
# Gas Prices
"""
Read text file with the average weekly gas prices in the United States.
Each line in the file contains the average price for a gallon of gasoline on a
specified date:
-------------------
MM-DD-YYYY : Price
-------------------
- Calculate average price per year
- Average price per month
- Highest and lowest prices per year: For each year in file, determine DATE and
AMOUNT for the lowest price, and the highest price
- List of prices, lowest to highest: Generate text file listing the dates and
prices, sorted from lowest price to highest
- List of prices, highest to lowest: Generate text file listing the dates and
prices, sorted from highet price to lowest
"""

def average_price_year(file, year, mode=None):
    # Calculates average price per year
    prices = [] # Empty list for adding the prices of each year
   
    # Iterates thru data, appending gas prices corresponding to given year
    for price in file:
        if year in price:
            prices.append(float(price[11:]))
   
    if mode == "avg":
        # Returns AVERAGE Gas prices for that year
        return sum(prices) / len(prices)

    elif mode == "high":    # Returns highest gas price for year
        return max(prices)

    elif mode == "low": # Returns lowest gas price for year
        return min(prices)

def average_price_month(file, month):
    # Calculates average price per month
    prices = []

    # Iterates thru months, appending gas prices correpsonding to given month
    for price in file:
        if month in price:
            prices.append(float(price[11:]))

    # Returns average gas prices for each month over the ten years or so
    return sum(prices) / len(prices)

def low_to_high():
    # Generates a text file with dates and prices, from lowest to highest
    pass

def high_to_low():
    # Generates a text file with dates and prices, from highest to lowest
    pass

def main():
    file = open("gas_prices.txt", "r").read().split()
    breakpoint()

if __name__ == "__main__":
    main()
