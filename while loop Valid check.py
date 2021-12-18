# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:52:10 2021

@author: kevmm
"""

import math

def getValidNumber():
    valid = True
    num = int(input("Input age (1 - 90): "))
    while (num < 1 or num > 90):
        valid = False
        if not valid:
            num = int(input("Bad Input, Input age (1 - 90): "))
            return num
        
number = getValidNumber()
print(number)
    