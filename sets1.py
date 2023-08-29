# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:14:13 2023

@author: HP
"""

set1={1,2,3,4,5,6,7}
print(set1)
set1.add(8)
print(set1)
set2={4,5,6,7}
print(set2)
set1.update(set2)
print(set1)
set2.update(set1)
print(set2)
print(set1.union(set2))


print(set1.intersection(set2))