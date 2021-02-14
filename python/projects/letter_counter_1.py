# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:43:21 2021

@author: C7169-Deniz
"""

"""
This simple program finds out the amount of each character in a given sentence.
"""

print("\This simple program finds out the amount of each character in a given sentence.")

given_sentence = input("\nPlease enter your sentence: ")

character_dict = {}

for i in given_sentence:
    keys = character_dict.keys() # With the help of this we can control the if
    # statement, assign a character and increment the value if it is more than one
    if i in keys:
        character_dict[i] += 1
    else:
        character_dict[i] = 1

print(character_dict)

# Many thanks Joseph can. Not only you love us, we love you too.
# With small touches you teach us many wonderful things with one stroke.
# Take care of yourself. Stay healthy and happy.
