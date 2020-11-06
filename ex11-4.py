# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 02:46:31 2020

@author: Ouso
"""

'''
Exercise 11-4.
If you did Exercise 10-7, you already have a function named has_duplicates that
takes a list as a parameter and returns 
True if there is any object that appears more than once in the list.
Use a dictionary to write a faster, simpler version of has_duplicates.
'''

def has_duplicates(alist):
    counts = {}
    for item in alist:
        if item not in counts:
            counts[item]=1
        else:
            return True
    return False

           
    
test_list1 = [1,4,6,1]
print(has_duplicates(test_list1))

test_list2 = [1,4,6]
print(has_duplicates(test_list2))