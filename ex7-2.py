# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 00:50:07 2020

@author: Ouso
"""

'''
Ex7-2.
The built-in function eval takes a string and evaluates it using the Python interpreter.
For example:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Write a function called eval_loop that iteratively prompts the user, 
takes the resulting input and evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of
the last expression it evaluated.
'''
def eval_loop():
    s = input('insert expression to evaluate \n')
    while s != 'done':
        print(eval(s))
        s = input('insert expression to evaluate \n')

        
eval_loop()