# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:27:19 2023

@author: HP
"""


# Python code to demonstrate naive method
# to compute factorial
n = int(input("n"))
fact=1
for i in range(1, n+1):
    fact = fact * i
print(fact)