# -*- coding: utf-8 -*-
"""
Created on Thu May 20 02:18:47 2021

@author: Daniel
"""

# Write code using find() and string slicing to extract the number at the end
# of the line below. Convert the extracted value to a floating point number
# and print it out
text = "X-DSPAM-Confidence:    0.8475"

pos0 = text.find('0')

print(float(text[pos0:]))