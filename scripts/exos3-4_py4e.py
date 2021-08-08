# -*- coding: utf-8 -*-
"""
Created on Wed May 12 01:27:24 2021

@author: Daniel
"""

def computepay(hours,rate):
    if hours > 40 :
        payunder40 = 40 * rate
        payupper40 = (hours - 40) * (1.5 * rate)
        return payunder40 + payupper40
    elif hours >=0 and hours <= 40 :
        return rate * hours
    elif hours < 0 :
        return "Negative hours input"
    else :
        return "Not a number in computepay"

snbrhours = input("Enter Nbr of hours : ")  
snbrrate  = input("Enter rate : ")
try :
    fnbrhours = float(snbrhours)
    fnbrrate  = float(snbrrate)
except :
    print("Not a number in try except")
    quit()
pay = computepay(fnbrhours, fnbrrate)
print("Pay",pay)