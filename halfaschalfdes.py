# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:03:36 2023

@author: HP
"""

list1 = [1,4,3,2, 5, 6, 7, 8, 9, 10]
list2 = []
for x in list1:
        x=x/2 
        list2.append(x) 
        list2.sort()
print(list2)
        