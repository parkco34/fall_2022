#!/usr/bin/env python
# Cory Parker
# CPT101
#10 Feet To Inches


"""
Function to take in feet as user argument and returns
the number of inches.
"""

def feet_to_inches(feet):
    return 12 * feet

if __name__ == "__main__":
    print(feet_to_inches(float(input("\nEnter the number of feet: \n"))))
