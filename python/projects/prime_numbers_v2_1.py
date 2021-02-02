# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:32:34 2021

@author: C7169-Deniz
"""

"""
Task : Print the prime numbers which are between 1 to entered limit number (n).
"""
print("\nThis simple program gives you all the prime numbers between \
      \n1 to the number you decided!\n\
      \nFor instance, if you give 50 as an input argument, the program gives\
      \nyou all the prime numbers between 1 and 50 as a list: \
      \n[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]")


number = input("\nPlease enter the limit number: ")

while True: # while block checks if the given number is a valid type
    if number.isdigit():
        break
    else:
        number = input("\nIt is an invalid entry. Please don't use non-numeric,\
                       \nfloat, or negative values! Please enter the number: ")

number = int(number)
list_1=[]
for i in range(1, number+1):
    list_2=[]    
    for j in range(1,i+1):
        if i % j == 0:
            list_2.append(j)         
    
    if (len(list_2) == 2):
        list_1.append(i)

print("\n", list_1, sep="")
