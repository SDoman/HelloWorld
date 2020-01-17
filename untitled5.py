# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:17:11 2020

@author: Admin
"""

annual = float(input("Enter annual salary: "))
percSaved = float(input("Enter the % saved: "))
totCost = float(input("Enter total cost of house: "))

downPperc = 0.12
rate = 0.05
current = 0
month = 0

monthSalary = annual/12
portionSaved = monthSalary * percSaved
downPay = totCost * downPperc

while downPay > current:
    current = current*(1 + rate/12)
    current = current + portionSaved 
    #print(current)
    month += 1
    
print(month)