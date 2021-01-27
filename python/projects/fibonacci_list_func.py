# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 04:22:33 2021

@author: 7169-Deniz
"""
"""
This simple function calculates the fibonacci numbers.
It prints out the Fibonacci numbers as a list. You should call the function 
with desired length. 

For instance: If you want to calculate the first 10 Fibonacci numbers,
you can call the function as folows: calc_fib_list(10)
"""

len_of_list = input("\nHow many Fibonacci numbers you want to calculate: ")

while True: # while block checks if the given number is a valid type
    if len_of_list.isdigit():
        break
    else:
        len_of_list = input("\nIt is an invalid entry. Don't use non-numeric, float, "\
                  "or negative values! Please enter the number: ")
            
len_of_list = int(len_of_list)

def calc_fib_list(len_of_list):
    fibonacci_list = [1, 1] # You should give the first two elements. All the
    #calculations base on these two elements.
    
    if len_of_list >= 2:        
        for i in list(range(1, len_of_list-1)):
            first_num = fibonacci_list[i-1]
            second_num = fibonacci_list[i]
            fibonacci_list.append(first_num + second_num)
        print(f"The first {len_of_list} Fibonacci numbers are: \n{fibonacci_list}")
        
    elif len_of_list == 1:
        print(f"The first Fibonacci numbers is: \n{fibonacci_list[:len_of_list]}")
        
    else:
        print("You choosed 0, there is nothgint to print out!")
        
calc_fib_list(len_of_list)