# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 01:04:44 2021

@author: Daniel
"""

"""
9.4:
Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address
to a count of the number of times they appear in the file. After the dictionary
is produced, the program reads through the dictionary using a maximum loop to 
find the most prolific committer."""

fname = input("Enter file name: ")
handle = open(fname)
committers = dict()
for line in handle:
    if line.startswith("From "):        
        words = line.split()        
        if (len(words) < 2):
            continue        
        committers[words[1]] = committers.get(words[1],0) + 1        
maxCommits = None
bestCommitter = None
minCommits = None
worstCommitter = None
for committer, commits in committers.items():
    if (maxCommits is None) or (commits > maxCommits) :
        maxCommits = commits
        bestCommitter = committer
    if (minCommits is None) or (commits < minCommits) :
        minCommits = commits
        worstCommitter = committer
#print(f"Most prolific committer: {bestCommitter} with {maxCommits} commits")
#print(f"Less prolific committer: {worstCommitter} with {minCommits} commits")       
print(f"{bestCommitter} {maxCommits}")        