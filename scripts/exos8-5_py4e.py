# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:48:56 2021

@author: Daniel
"""

"""
8.5 Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the
line (i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

count = 0
fname = input("Enter file name: ")
fhandle = open(fname,'r')
for line in fhandle:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        mail = words[1]
        count = count + 1
        print(mail)                               
print("There were", count, "lines in the file with From as the first word")
