#!/usr/bin/env python
# Cory Parker
# CPT101
# US Population
"""
File contains the US population in the thousands, during the years 1950-1990,
corresponding to each line in the file
Program reads the file's contents into a list, displaying:
    - Average annual change in population during the period
    - Year with the greatest increase in population during period
    - Year with the smalles increase in population during the time period

A secondary list is created with popluation changes from one year to the next,
where one could search for average, max and min values
"""
def get_list(file_obj):
    # Takes a file object and returns the contents as a list
    return [int(i) for i in file_obj.read().split()]

def get_average(_list):
    # Returns average of list as integer
    prev = _list[0]
    annual_change_list = []

    for i in range(1, len(_list)+1):
        if len(_list) == i:
            break

        diff = abs(_list[i] - prev)
        annual_change_list.append(diff)
        prev = _list[i]

    return int(sum(annual_change_list)/ len(annual_change_list))

def get_max_increase(_list):
    # Returns the maximnum increase in population
    return max(_list)

def get_smallest_increase(_list):
    # Returns the smallest increase in population
    return min(_list)

def main():
    file = open("USPopulation.txt", "r") # Reads file
    ann_population = get_list(file)
    file.close()    # Close file

    print(f"""
Average: {get_average(ann_population)}\n
Maximum population increase: {get_max_increase(ann_population)}\n
Minimum population increase: {get_smallest_increase(ann_population)}\n
          """)

if __name__ == "__main__":
    main()

