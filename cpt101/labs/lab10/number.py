#!/usr/bin/env python
# Cory Parker
# CPT101
# Number Analysis
"""
User input for a series of 20 numbers, storing the numbers in a list.
Output should be:
    - lowest element in list
    - Highest element in list
    - Total of the numbers in the list
    - Average of the numbers in the list

- All numbers entered can be assumed to be integers
- Returns a complete list
"""

def get_list():
    # Creates list with the 20 user input values
    return [int(input("\nPlease enter 20 integers:\n")) for i in range(20)]

def lowest(user_list):
    # returns lowest number in list
    return min(user_list)

def highest(user_list):
    # Returns the highest number in the list
    return max(user_list)

def total(user_list):
    # returns the total fo the numbers in the list
    return sum(user_list)

def average(user_list):
    # Returns the Average of the numbers in the list
    return int(total(user_list) / len(user_list))

def main():
    numbers = get_list()    # User-defined list
    print(f"""
\nUser-defined list: {numbers}\n
Lowest Element: {lowest(numbers)}\n
Highest Element: {highest(numbers)}\n
Total: {total(numbers)}\n
Average: {average(numbers)}\n
          """)

if __name__ == "__main__":
    main()
