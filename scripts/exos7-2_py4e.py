# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 01:09:08 2021

@author: Daniel
"""
"""
7.2 Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
import re

pattern = "(\d+\.*\d*)"
linemotif = "X-DSPAM-Confidence:"

fname = input("Input file name: ")
try:
    fh = open(fname,"r")
except:
    print("incorrect value for file name")
    quit()
    
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if line.startswith(linemotif):
        count = count + 1
        match = re.search(pattern, line)
        if match:
            total = total + float(match.group())
            #print(float(match.group()))
            
average = total / count
print("Average spam confidence:",average)
            
        