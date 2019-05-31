# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:33:48 2019

@author: HeYu5
"""

def move_zeros(array):
    #your code here
    cnt = 0
    res = []
    for i in array:
        if i == 0:
            cnt += 1
        else:
            res.append(i)
    a = [0 for i in range(cnt)]
    return res + a

a = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
print move_zeros(a)