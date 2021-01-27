# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 01:19:38 2021

@author: Deniz
"""

"""
This simple program finds out if a given number is an "Armstrong Number".

An n-digit number that is the sum of the nth powers of its digits is called
an n-Armstrong number.

Examples :
    
371 = 3**3 + 7**3 + 1**3
9474 = 9**4 + 4**4 + 7**4 + 4**4
93084 = 9**5 + 3**5 + 0**5 + 8**5 + 4**5
"""

given_number = input("\nPlease enter a number to check if it is "\
                             "an 'Armstrong Number' or not: ")

while True: # while block checks if the given number is a valid type
    if given_number.isdigit():
        break
    else:
        given_number = input("\nIt is an invalid entry. Don't use non-numeric, float, "\
                  "or negative values! Please enter the number: ")
            
def is_armstrong(given_number):        
    given_num_list = list(given_number)
    total = 0
    for i in range(len(given_num_list)):
        total += int(given_num_list[i])**(len(given_num_list))
    return(total)

if is_armstrong(given_number) == int(given_number):
    print(int(given_number), "is an Armstrong number.")
else:
    print(int(given_number), "is not an Armstrong number.")
   
