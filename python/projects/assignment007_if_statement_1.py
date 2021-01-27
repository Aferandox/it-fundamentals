# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 01:35:27 2021

@author: Deniz
"""

name = "deniz"
password = "W@12"

name_entered = str(input("Please enter your name: "))

if name_entered.lower() == name:
    print("\nHello, {}! The password is {}".format(name.capitalize(), password))
else:
    print("\nHello, user! See you later.")

