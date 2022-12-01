#!/usr/bin/env python
# Cory Parker
# CPT101
# Average Steps Taken
"""
Reads file, then displays the average steps taken for each month
"""

def avg_steps(month):
    steps = []
    file = open("steps.txt", "r")   # Create file object
    contents = file.read()
    file.close()    # Close file object
    step_list = [int(i) for i in contents.split()]    # Creates a list of the steps from the txt
    # Returns the average steps pr day for the month
    for day in range(month):
        steps.append(step_list[day])

    return int(sum(steps) / month)

def main():
    # 
    # Days in the sorted months
    MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUNE", "JULY", "AUG", "SEPT",
             "OCT", "NOV", "DEC"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for day in days:    # Iterate thru the days corresponding to the month
        print(f"{avg_steps(day)}\n")

if __name__ == "__main__":
    main()

