#!/usr/bin/env python

"""
Cory Parker
14.) Body Mass Index
-----------------------------
Calculates the person's body mass index (BMI) to determine
if their overweight or underweight.

If the values provided by the user indicate that the person is
in the overweight category, then calculate and provide the amount of weight that is
needed to lose to get down into the optimal category

Formula:
BMI = weight * 703 / heaight^2
weight: In pounds (LBS) (int)
height: In inches (in) (int)
-----------------------------
===================================
- User input (Assumed to be positive numbers...)
- if-else to determine optimal BMI
- print
===================================
"""

weight = float(int(input("\nEnter your weight in pounds (lBS): \n")))
height = float(input("\nenter your height  in inches (in)\n"))

bmi = weight * 703 / (height)**2
print(f"\nBMI = {bmi: .2f}")

if bmi > 25:
    print(f"\nOverweight\nLose: {bmi - 25: .2f} lbs")

elif bmi <= 25 and bmi >= 18.5:
    print("\nOptimal weight\n")

else:
    print("\nUnder weight\nGain: {(37/2) - bmi: .2f} lbs")



