# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:14:49 2020

@author: Ouso
"""

def do_twice(f,val):
    ''' calls a function object twice on a value argument
    f is a function object 
    val is a value argument
    '''
    f(val)
    f(val)
    
def print_spam():
    ''' prints "spam"
    '''
    print('spam')

def print_twice(bruce):
    ''' prints a value twice
    bruce  a value to print 
    '''
    print(bruce)
    print(bruce)
    
def do_four(f,val):
    ''' calls a function object 4 times on a value argument
    f is a function object 
    val is a value argument
    '''
    do_twice(f,val)
    do_twice(f,val)
        

do_twice(print_twice,'spam') # print spam 4 times
do_four(print,'spam') #print spam 4 times