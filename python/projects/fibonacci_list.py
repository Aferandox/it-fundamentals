# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 03:31:33 2021

@author: 7169-Deniz
"""

fibonacci_list = []
fibonacci_list.append(1)
fibonacci_list.append(1)
len_of_list = 10


for i in list(range(1, len_of_list-1)):
    first_num = fibonacci_list[i-1]
    second_num = fibonacci_list[i]
    fibonacci_list.append(first_num + second_num)
   
print(fibonacci_list)
    