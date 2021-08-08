# -*- coding: utf-8 -*-
"""
Created on Thu May 13 01:08:48 2021

@author: Daniel
"""

smallest = None
largest  = None

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    
    try:
        ival = int(sval)
    except:
        print('Invalid input')
        continue
    
    # Retrieving the smallest
    if smallest is None:
        smallest = ival
    elif ival < smallest:
        smallest = ival
     
    # retrieving the largest
    if largest is None:
        largest = ival
    elif ival > largest:
        largest = ival
        
print('Maximum is', largest)
print('Minimum is', smallest)
