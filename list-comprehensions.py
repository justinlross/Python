# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 08:16:04 2019

@author: Justin
"""

string = "Use a dictionary comprehension to count the length of each word in a sentence."

counter = [len(word) for word in string.split(' ')]

print(counter)


#Challenge: Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
divBy = [number for number in range(1,1001) if True in [True for divisor in range(2,10) if number % divisor == 0]]

print(divBy)