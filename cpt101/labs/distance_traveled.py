#!/usr/bin/env python
# ====================================
# MY TEST:
import test_distance_traveled as Test
assert Test.test_distance_traveled()
# ====================================

"""
Cory Parker
Distance Traveled
Lab 5
-------------------------------------------------
Asking user for the speed of car (mph), and the number of
hours traveled.  It should then use a loop to display 
the distnace the car traveled.
-------------------------------------------------
EXAMPLE:
    v = float(input("What's the speed of your car? (mph) \n")) # 40
    t = float(input("How many hours has you car traveled? \n")) # 3

OUTPUT:

  Hour       Distance Traveled
  ----       -----------------
    1           40
    2           80
    3           120
-------------------------------------------------
"""

speed = float(input("What's the speed of your car? \n"))    # Speed (mph)
travel_time = float(input("How many hours has your car traveled? \n"))    # Time (hrs)
print(f"\nHour           Distance\n")   # Header

for i in range(1, int(travel_time)+1):
    print(f"{i:<25}", end=" ")
    print(f"{int(speed*i)}\n")




