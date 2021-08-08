# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 00:32:42 2021

@author: Daniel
"""

fname = input("Enter file name: ")

try:
    fh = open(fname,"r")
except:
    print("incorrect value for file name")
    quit()
    
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)