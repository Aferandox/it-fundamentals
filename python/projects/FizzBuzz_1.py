# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:59:10 2021

@author: C7169-Deniz
"""
"""
Task : Print the FizzBuzz numbers.

This simple program prints the numbers from 1 to 100 inclusively following 
these instructions:
    
1. If a number is multiple of 3, print "Fizz" instead of this number,
2. If a number is multiple of 5, print "Buzz" instead of this number,
3. For numbers that are multiples of both 3 and 5, print "FizzBuzz",
4. Print the rest of the numbers unchanged.
5. Output each value on a separate line.

"""

numbers = list(range(1, 101))

for i in numbers:
    if i%15 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        if i%5 == 0:
            continue
        else:
            print("Fizz")
    elif i%5 == 0:
        if i%3 == 0:
            continue
        else:
            print("Buzz")      
    else:
        print(i)