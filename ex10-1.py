# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 01:59:32 2020

@author: Ouso
"""

'''
Exercise 10-1.
Write a function called nested_sum that takes a list of lists of integers 
and adds up the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''
def nested_sum(lists):
    sums =0
    for alist in lists:
        sums += sum(alist)

    return sums
