# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:49:38 2023

@author: ManiKanDaN
"""

l=[1,2,3,4,6,5,4,2,1]
print(set([x for x in l if l.count(x)>1]))
    