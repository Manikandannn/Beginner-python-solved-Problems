# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:22:35 2023

@author: ManiKanDaN
"""

n=int(input("Enter the fibonacci series for till :"))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+first
    
    #(or)
def F(n):
    if n==0: return 0
    elif n==1:return 1
    else:return F(n-1)+F(n-2)
for i in range (0,12):
    print(F(i))
    