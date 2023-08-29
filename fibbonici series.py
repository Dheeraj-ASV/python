# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:16:00 2023

@author: HP
"""
n =int(input("enter n"))
num1 =int(input("enter num1"))
num2 =int(input("enter num2"))
next_number = num2 
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()