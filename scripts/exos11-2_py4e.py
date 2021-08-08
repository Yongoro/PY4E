# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 01:03:39 2021

@author: Daniel'
"""

"""
In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.


extract:
    
Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative 
7 and rewarding activity.  You can write programs for 
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that 
everyone needs to know how to program ...

sample file name : regex_sum_42.txt
assignment file name: regex_sum_1244867.txt

"""
"""
import re

fname = input("Enter file name: ")
handle = open(fname)
sum = 0
for line in handle:
    match = re.findall("\d+", line.rstrip())
    if len(match) > 0:
        for num in match:            
            sum = sum + int(num)
print(sum)
"""

# using list comprehension
import re

print( sum( [ int(num) for num in re.findall('[0-9]+', open('regex_sum_42.txt','r').read()) ] ) )
