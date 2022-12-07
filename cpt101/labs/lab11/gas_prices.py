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

def average_price_year(year):
    # Calculates average price per year
    pass

def average_price_month(month):
    # Calculates average price per month
    pass

def high_low_price_year(year):
    # For each year, fin date, highest/lowest price
    pass

def low_to_high():
    # Returns a list of prices, from lowest to highest, generating a text file
    pass

def high_to_low():
    # Returns a list of prices, from highest to lowest generating a text file
    pass

def main():
    file = open("gas_prices.txt", "r").read().split()
    breakpoint()

if __name__ == "__main__":
    main()
