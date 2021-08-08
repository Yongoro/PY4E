# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:20:41 2021

@author: Daniel
"""

hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("You have entered bad values")
    quit(-1)  
    
print(h,r)    
if h <= 40:
    pay = h * r
else:
    pay1 = 40 * r
    pay2 = (h - 40) * (1.5 * r)
    pay = pay1 + pay2
print("Pay",pay)    