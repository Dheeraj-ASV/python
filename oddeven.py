# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:56:02 2023

@author: HP
"""
y = int(input("Enter the number of integers: "))
n = int(input("Enter a number: "))

list1 = []
for num in range(n, y):
    list1.append(num)
    
list2 = []

for i in list1:
    if i % 2 == 0:
        list2.append(i)

list3 = [x for x in list1 if x not in list2]

print(list1)
print(list2)
print(list3)


        
        
        