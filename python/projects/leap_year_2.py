# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 00:59:17 2020

@author: C7169-Deniz
"""

"""
Task:

Find out if a given year is a "leap" year.

In the Gregorian calendar, three criteria must be taken into account \
\nto identify leap years:
The year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is not a leap year; unless...
The year is also evenly divisible by 400. Then it is a leap year.
According to these rules, the years 2000 and 2400 are leap years, \
\nwhile 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
Write a Python program that;
Takes a 4-digit year from the user,
Prints True if the given year by the user is a leap year, prints False otherwise.

"""


print("\nThis small program calculates, if a given year a 'leap' year is.")

while True:
    try:
        year = int(input("\nPlease enter the year only in four digits: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

if ((year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)):
    print("{} is a 'leap' year.\n".format(year))
    print("True")
elif ((year % 4 == 0) and (year % 100 != 0)):
    print("{} is a 'leap' year.\n".format(year))
    print("True")
else:
    print("{} is not a 'leap' year.\n".format(year))
    print("False")
