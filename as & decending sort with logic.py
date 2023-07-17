# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:11:36 2023

@author: ManiKanDaN
"""
data_list=[12,7,98,8,64,8,73,38,54,2,3,1]
new_list=[]
while data_list:
    minimum=data_list[0]
    for x in data_list:
         if  x>minimum:
             minimum=x
    new_list.append(minimum)
    data_list.remove(minimum)
print(new_list)
new_list.sort()
print(new_list)