#!/usr/bin/env python
# Cory Parker
# Project 1
# CPT101

"""
Write a program that asks a user to enter a time value in seconds and then works as follows:
    - If the user inputs more than a days’ worth of seconds, then output the number of days, hours, minutes, and seconds.  (i.e.  86,500 seconds would report 1 day, 0 hours, 1 minute, 40 seconds)
    - If the user inputs less than a days’ worth of seconds but more than an hour’s, then output the number of hours, minutes, and seconds.  (i.e.  7,250 seconds would report 2 hours, 0 minute, 50 seconds)
    - If the user inputs less than a hours’ worth of seconds but more than an minute’s, then output the number of minutes, and seconds.  (i.e.  680 seconds would report 11 minute, 20 seconds)
    - Otherwise it just outputs the number of seconds back.
Start and stop this program with friendly messages explaining what the program in attempting to do and letting the user know that it is finished.
=======================================================================================================================================
Structure Plan:
    1) Get user input as an integer
    2) Print initial values and use floor division to obtain number of days,
    hours, minutes, and the remainingn seconds, printing updated data along the
    way
    3) print results
=======================================================================================================================================
EXAMPLE:

    INPUT: 
        seconds = 86500

    OUPUT:
        Days: 3
=======================================================================================================================================
"""

seconds = int(input("Please enter a time value:\n"))
# Constants
MINS = 60
HR = 3600
DAY = 3600*24;

# Variables to store data
days = hours = minutes = 0

print(f"""
Initial Values:
seconds: {seconds}\n
Hours: {hours}\n
Minutes: {minutes}\n
Days: {days}\n
""")
# Decisions
if (seconds//DAY) > 0:
    days = seconds // DAY
    print(f"""
Dividing seconds by the number seconds in a day\n
seconds: {seconds+ days*HR}\n
Days: {days}\n
New Seconds: {seconds}\n
          """)

if (seconds // HR) > 0:
    hours = seconds // HR
    seconds -= hours * HR
    print(f"""
Dividing seconds by the number seconds in a hours\n
seconds: {seconds + hours * HR}\n
Minutes: {hours}\n
New Seconds: {seconds}\n
          """)

if (seconds // MINS) > 0:
    minutes = seconds // MINS
    seconds -= minutes * MINS
    print(f"""
Dividing seconds by the number seconds in a minute\n
seconds: {seconds + minutes * MINS}\n
Minutes: {minutes}\n
New Seconds: {seconds}\n
          """)


print(f"""
\nDays: {days}\n
Hours: {hours}\n
Minutes: {minutes}\n
Seconds: {seconds}\n
      """)
