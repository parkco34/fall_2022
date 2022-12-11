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

def average_price_year(_list, year, mode=None):
    # Calculates average price per year, taking a list and the year
    prices = [] # Empty list for adding the prices of each year
   
    # Iterates thru data, appending gas prices corresponding to given year
    for price in _list:
        if year in price:
            prices.append(float(price[11:]))
   
    if not mode:
        # Returns AVERAGE Gas prices for that year
        return sum(prices) / len(prices)

    elif mode == "high":    # Returns highest gas price for year
        return max(prices)

    elif mode == "low": # Returns lowest gas price for year
        return min(prices)

def average_price_month(_list, month):
    # Calculates average price per month, taking in a list and month
    prices = []

    # Iterates thru months, appending gas prices correpsonding to given month
    for price in _list:
        if month in price:
            prices.append(float(price[11:]))

    # Returns average gas prices for each month over the ten years or so
    return sum(prices) / len(prices)

def low_to_high(_list):
    # Generates a text file with dates and prices, from lowest to highest
    _list.sort(key=lambda x: x.split(":")[1])

    return _list

def high_to_low(_list):
    # Generates a text file with dates and prices, from highest to lowest
    _list.sort(key=lambda x: x.split(":")[1], reverse=True)

    return _list

def main():
    file = open("gas_prices.txt", "r")  # Creates file object
    data = file.read().split()
    file.close()    # Close file objectj
    
    # Average gas prices per year loop
    year_set = set(item[6:10] for item in data)
    print("\nAVERAGE GAS PRICE PER YEAR:\n")
    for year in year_set:
        print(f"""
{year}: {round(average_price_year(data, year), 2)}
              """, end=" ")

    # Average monthly gas prices loop
    for month in range(1, 13):
        # If month starts with 0 or 1
        if month < 10:
            month = "0" + str(month)

        else:
            month = str(month)

        print("\nAVERAGE GAS PRICE PER MONTH\n")
        print(f"""
{month}: {round(average_price_month(data, month), 2)}
              """, end=" ")

if __name__ == "__main__":
    main()
