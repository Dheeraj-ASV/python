# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:16:43 2023

@author: HP
"""

x=int(input("enter your marks"))
print(x)
if x<0 or x>100:
    print("invalid marks")
elif x>=90:
    print("congrajulations")
    print("you have scored S grade")
elif x>=81 and x<91:
    print("congrajulations")
    print("you have scored A grade")
elif x>=71 and x<81:
     print("congrajulations")
     print("you have scored B grade")
elif x>=61 and x<71:
    print("congrajulations")
    print("you have scored C grade")
elif x>=51 and x<61:
    print("congrajulations")
    print("you have scored D grade")
elif x>=41 and x<51:
    print("Better luck next time")
    print("you have scored E grade")
elif x>=0 and x<40:
    print("odh le nettaga fail agge ni")