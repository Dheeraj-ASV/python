# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 10:59:09 2023

@author: HP
"""

n = int(input("Enter the number of elements: "))
lis = []

for i in range(n):
    x = input("Enter anything: ")
    lis.append(x)
    print(lis)

i = 0
while i < n:
    print("Hello", lis[i], "how are you?")
    i = i + 1

       