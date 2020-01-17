# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:57:57 2020

@author: Admin
"""

groupOfnum = [100, 2, 234]

currentMax = groupOfnum[0]

for high in groupOfnum:
    if high > currentMax:
        currentMax = high
print(currentMax) 

