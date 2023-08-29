# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:48:00 2023

@author: HP
"""

a=int(input("enter the value of a"))
print(a)
b=int(input("enter the value of b"))
print(b)
x=int(input("enter the value of x"))
print(x)
if (x==1):
    print("sum is")
    c=a+b
    print(c)
elif (x==2):
    print("diff is")
    c=a-b
    print(c)
elif (x==3):
        print("mul is")
        c=a*b
        print(c)
        d=a*b
        if(c==d):
            print("the mul is correct")
        else:
            print("the mul is wrong")
        
elif (x==4):
    print("div is")
    c=a/b
    print(c)


