# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:20:41 2021

@author: Daniel
"""

score = input("Enter Score: ")
try:
    scoref = float(score)
except:
    print("Incorrect score entered")
    quit()
    
if (scoref < 0.0 or scoref > 1.0):
    print("Error: out of range")
elif scoref >= 0.9:
    print("A")
elif scoref >= 0.8:
    print("B")
elif scoref >= 0.7:
    print("C")
elif scoref >= 0.6:
    print("D")
else:
    print("F")    