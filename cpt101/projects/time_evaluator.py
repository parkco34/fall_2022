#!/usr/bin/env python
"""
Write a program that asks a user to enter a time value in seconds and then works as follows:
    - If the user inputs more than a days’ worth of seconds, then output the number of days, hours, minutes, and seconds.  (i.e.  86,500 seconds would report 1 day, 0 hours, 1 minute, 40 seconds)
    - If the user inputs less than a days’ worth of seconds but more than an hour’s, then output the number of hours, minutes, and seconds.  (i.e.  7,250 seconds would report 2 hours, 0 minute, 50 seconds)
    - If the user inputs less than a hours’ worth of seconds but more than an minute’s, then output the number of minutes, and seconds.  (i.e.  680 seconds would report 11 minute, 20 seconds)
    - Otherwise it just outputs the number of seconds back.
Start and stop this program with friendly messages explaining what the program in attempting to do and letting the user know that it is finished.
=======================================================================================================================================
Structure Plan:
    1) 
=======================================================================================================================================
EXAMPLE:

    INPUT: 
        time_value = 86500

    OUPUT:
        Days: 3
=======================================================================================================================================
"""

time_value = int(input("Please enter a time value:\n"))
MINS = 60
HR = 3600


if DAYS > 1:
    print(f"""\n
Days: {DAYS}\n
Hours: {HOURS}\n

          """)
