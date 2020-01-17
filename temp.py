# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

annual = float(input("Enter annual salary: "))
percSaved = float(input("Enter the % saved: "))
totCost = float(input("Enter total cost of house: "))
raiseD = float(input("Enter raise %: "))

downPperc = 0.12
rate = 0.05
current = 0
month = 0

downPay = totCost * downPperc


while downPay > current:
    monthSalary = annual/12
    portionSaved = monthSalary * percSaved
    
    current = current*(1 + rate/12)
    current = current + portionSaved 
    print(current)
    month += 1
    if month%6 == 0:
        annual = annual + (annual*raiseD)
        
        

print(month)

   