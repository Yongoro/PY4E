# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:03:51 2021

@author: Daniel
"""

"""
8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in the list and
if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical
order. You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

correct = False
result = list()

while not correct:
    try:
        fname = input("Enter file name: ")
        fhandle = open(fname,'r')
        correct = True
        for line in fhandle:
            line = line.strip()
            words = line.split()
            for word in words:
                if word not in result:
                    result.append(word)            
    except:
        print("file not found! try another name")
        continue
    
print("Before sorting: ")
print(result)
result.sort()
print("After sorting: ")
print(result)
    
