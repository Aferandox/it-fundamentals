# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 02:16:15 2021

@author: C7169-Deniz
"""


print("\nThis simple program shows you, which risk group you are belonging \
\nto for Covid-19. There are 8 groups in total and the group 8 represents \
\nthe highest risk group. I wish you all the best. Stay at home, stay safe!\n")

cigarette_age75 = ""
severe_chronic_disease = ""
immune_weak = ""

while ((cigarette_age75 == 'y') or (cigarette_age75 == 'n')) == False:
    cigarette_age75 = input("Are you cigarette addict older than 75?\
    \nPlease press y for Yes and n for No: ")

while ((severe_chronic_disease == 'y') or (severe_chronic_disease == 'n')) == False:
    severe_chronic_disease = input("Do you have any severe chronic diseases? \
    \nPlease press y for Yes and n for No: ")

while ((immune_weak == 'y') or (immune_weak == 'n')) == False:
    immune_weak = input("Is your immune system too weak?\
    \nPlease press y for Yes and n for No: ")

a = cigarette_age75
b = severe_chronic_disease
c = immune_weak
def risk_calculator(a, b, c):
    print("\n\
    ------------------------------\n\
    Group 8 = Smoking, more than 75 years old, has severe chronic disease \
    \nand has a weak immune system.\n\
    Group 7 = Smoking, more than 75 years old, has severe chronic disease \
    \nand has a STRONG immune system.\n\
    Group 6 = Smoking, more than 75 years old, has NO severe chronic disease \
    \nand has a weak immune system.\n\
    Group 5 = Smoking, more than 75 years old, has NO severe chronic disease \
    \nand has a STRONG immune system.\n\
    Group 4 = Younger than 75 or not smoker, has severe chronic disease \
    \nand has a weak immune system.\n\
    Group 3 = Younger than 75 or not smoker, has severe chronic disease \
    \nand has a STRONG immune system.\n\
    Group 2 = Younger than 75 or not smoker, has NO severe chronic disease \
    \nand has a weak immune system.\n\
    Group 1 = Younger than 75 or not smoker, has NO severe chronic disease \
    \nand has a STRONG immune system.\n\
    ------------------------------\
    ")        
    
    if (a == 'y'):
        if (b == 'y'):
            if (c == 'y'): #Group8
                print("\nYou belong the Group 8. It is the riskiest group. \
                \nYou are smoking, older than 75, have chronic disease, and \
                \na weak immune system. You should close the door, and read books \
                \nfor the next 6 months. Which is a great opportunity to improve \
                \nyourself.\n")
            elif(c == 'n'): #Group7
                print("\nYou belong the Group 7. Your immune systeym is good, \
                \nbut it doesn't mean you are not under high risk. Because \
                \nyou are smoking, older than 75 and have chronic disease. \
                \nyou should be very careful.\n")
        elif (b == 'n'):
            if (c == 'y'): #Group6
                print("\nYou belong the Group 6. You don't have any severe chronic \
                \ndisease, which is good. But still you are under great risk, \
                \nbecause you are smoking, older than 75 and have a week immune \
                \nsystem.\n")
            elif(c == 'n'): #Group5
                print("\nYou belong the Group 5. You don't have any severe chronic \
                \ndisease, which is good, and have a strong immune system. But still \
                \nyou are under risk, because you are smoking and older than 75 \
                \ntherefore, you should be careful.\n")
    elif (a == 'n'):
        if (b == 'y'):
            if (c == 'y'): #Group4
                print("\nYou belong the Group 4. You are younger than 75 or not \
                \nsmoking. But you have severe chronic disease and a weak immune \
                \nsystem. Therefore you should be careful.\n")
            elif(c == 'n'): #Group3
                print("\nYou belong the Group 3. You are younger than 75 or not \
                \nsmoking, and have a STRONG immune system. But you have severe \
                \nchronic disease. Therefore, you should still be careful.\n")
        elif (b == 'n'):
            if (c == 'y'): #Group2
                print("\nYou belong the Group 2. You are younger than 75 or not \
                \nsmoking, and have NO chronic disease, which is good, but you have \
                \na weak immune system, which makes you vulnerable. Being careful \
                \nwouldn't hurt.\n")
            elif(c == 'n'): #Group1
                print("\nYou belong the Group 1. You are younger than 75 or not \
                \nsmoking, and have NO chronic disease, which is good, you also \
                \nhave a STRONG immune system. But there are cases like you, \
                \nand had great problems with Covid-19. Being careful doesn't hurt.\n")
    else:
        print("Something went wrong!!!")                
        
risk_calculator(a, b, c)      
                
