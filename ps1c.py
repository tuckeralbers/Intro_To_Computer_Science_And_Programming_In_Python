#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:29:06 2020

@author: tuckeralbers
"""


annual_salary = float(input("Please enter your current salary: "))

total_cost = 1000000.0
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = total_cost*portion_down_payment
r = 0.04
savings_rate = False
initial_rate = 0.00
max_rate = 1.00
steps = 0
while savings_rate == False:
    steps += 1
    portion_saved = (max_rate + initial_rate)/2
    current_savings = 0.0
    current_salary = annual_salary
    for i in range(0,37,1):
        
        current_savings = current_savings+(current_savings*r)/12 + portion_saved*current_salary/12
        if i%6 == 0 and i > 0:
            current_salary = current_salary + current_salary*semi_annual_raise
         
    if portion_saved >= 0.9999:
        print("Get a new Job. You wont have enough in 3 years!")
        savings_rate = True
    elif current_savings < down_payment - 100:
        #print('Amount Saved: ', current_savings)  
        new_rate = (max_rate + portion_saved)/2
        initial_rate = portion_saved
        portion_saved = new_rate
        
    elif current_savings > down_payment + 100:
        #print('Amount Saved: ', current_savings)  
        new_rate = (initial_rate + portion_saved)/2
        max_rate = portion_saved
        portion_saved = new_rate
    else:
        print("This is the Amount Saved: ", current_savings)
        print("This is the savings rate: ", portion_saved)
        print("These are the number of steps", steps)
        savings_rate = True
    
    
