# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:16:19 2020

@author: Ouso
"""

'''
Exercise 5-4.
What is the output of the following program? Draw a stack diagram that shows the
state of the program when it prints the result.

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)

1. What would happen if you called this function like this: recurse(-1, 0)?

2. Write a docstring that explains everything someone would need to know in 
order to use this function (and nothing else).
'''
def recurse(n, s):
    ''' a recurseive function that evaluates and prints the sum from 0 to n 
    added to it another number s
    
    s+sigma(n) from 0 to n
    
    n : a positive integer 
    s: a real number
    
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)


#Ans. 1 recurse(-1,0), will cause infinite recursion and RecursionError
#RecursionError: maximum recursion depth exceeded in comparison'''

print(
'''Ans 2. stack diagram

__main__


countdown

n --> 3
s --> 3

countdown

n --> 2
s --> 5

countdown

n --> 1
s --> 6

countdown

n --> 0
s --> 6 ''')