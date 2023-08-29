# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:33:55 2023

@author: HP
"""

a=int(input("enter value of a="))
print(a)
b=int(input("enter value of b="))
print(b)
print("and op is",a&b)
print("or op is",a|b)
print("xor op result is",a^b)
print("negation is",~(a&b),~(a|b),~(a^b))
print("left shift is",a<<b,b<<a)
print("right shift is",a>>(b),b>>a)
