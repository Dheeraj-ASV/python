# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:02:13 2023

@author: HP
"""
a=int(input("enter value of a"))
print(a)
b=int(input("enter value of b"))
print(b)
print("sum is",a+b)
if (a-b<=0):
    print("negative value")
else:
    print("difference is",a-b)

print("multiplication result is",a*b)
c=a%b
print("divided result is",c)
print("reminder is",a%b)
print("exponent is",a**(b))
d=int(input("enter value of d"))
print(d)
e=a+b-c/d
print("floor plan",e)
