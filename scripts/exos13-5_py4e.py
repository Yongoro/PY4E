# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 23:12:13 2021

@author: Daniel
"""

'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to 
http://www.py4e.com/code3/json2.py. The program will prompt for a URL, 
read the JSON data from that URL using urllib and then parse and extract the 
comment counts from the JSON data, compute the sum of the numbers in the file 
and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process 
for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1244872.json (Sum ends with 44)
You do not need to save these files to your folder since your program will read 
the data directly from the URL. Note: Each student will have a distinct data url
for the assignment - so only use your own data url for analysis.

Data Format
The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
'''
from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0  
url = input('Enter url: ') 
print('Retrieving', url)
data = urlopen(url, context=ctx).read()

info = json.loads(data.decode())
comments = info['comments']

for item in comments:
    sum = sum + int(item['count'])
print(f"Sum={sum}")