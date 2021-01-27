# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:18:40 2021

@author: Deniz
"""

"""
This simple program finds out if the given number is a prime number or not.
"""

number = int(input("\nPlease enter a number: "))

list_div_result=[]
for i in range(1,number+1):
    if number % i == 0:
        list_div_result.append(i)        

if (len(list_div_result) > 2):
    print("{} is a not prime number!".format(number))
elif (len(list_div_result) == 2):
    print("{} is a prime number!".format(number))
