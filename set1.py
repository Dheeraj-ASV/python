# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:39:49 2023

@author: HP
"""

set1 = {1,2,3,4,5,6}
set2 = {7,8,9,10}
set3 ={}
set4 ={}
#set1.update(set2)
#print(set1)
#set1.discard("Ball")
#print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
set3 = set2.copy()
print(set3)
set2.update(set1)
print(set2)