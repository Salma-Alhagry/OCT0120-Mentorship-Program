# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 02:33:56 2020

@author: Ouso
"""

'''
Exercise 10-2.
Write a function called cumsum that takes a list of numbers and 
returns the cumulative sum; that is, a new list where the ith element 
is the sum of the first i+1 elements from the original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
'''
def cumsum(alist):
    cum_sum = []
    for i in range(len(alist),0,-1):
        cum_sum.append(sum(alist[:i]))
    return cum_sum[::-1]