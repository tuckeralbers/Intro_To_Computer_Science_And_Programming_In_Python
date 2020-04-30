#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:29:06 2020

@author: tuckeralbers
"""

annual_salary = float(input("Please enter your current salary: "))
portion_saved = float(input("Please enter the portion of salary you wish to save: "))
total_cost = float(input("Please enter your home price: "))
semi_annual_raise = float(input("Please enter your assumed 6 month raise: "))

portion_down_payment = 0.25


current_savings = 0

r = 0.04

months = 0
while current_savings < portion_down_payment*total_cost:
    current_savings = current_savings+(current_savings*r)/12 + portion_saved*annual_salary/12
    if months%6 == 0 and months > 0:
        print(annual_salary)
        annual_salary = annual_salary + annual_salary*semi_annual_raise
    months = months + 1
    
print("It will take this many months:",months)


