# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 01:03:39 2021

@author: Daniel'
"""

"""
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and
then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour,
print out the counts, sorted by hour as shown below.

"""

fname = input("Enter file name: ")
handle = open(fname)
hours_distro = dict()
for line in handle:
    if line.startswith("From "): 
        #print(line)
        words = line.split()        
        if (len(words) < 6):
            continue
        hours = words[5].split(':')
        hours_distro[hours[0]] = hours_distro.get(hours[0],0) + 1
        #print(hours_distro)
sorted_hours_distro = sorted([(k,v) for k,v in hours_distro.items()])     
for k,v in sorted_hours_distro:
    print(k,v)