# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 02:53:20 2020

@author: Ouso
"""

'''
Exercise 8-4.
The following functions are all intended to check whether a string contains 
any lower‐case letters, but at least some of them are wrong. For each function,
describe what the function actually does 
(assuming that the parameter is a string).
'''
def any_lowercase1(s):
    ''' Checks whether the first letter is lower or not
    s: string
    '''
    for c in s:
        if c.islower():
            print(c)
            return True
        else:
            return False
def any_lowercase2(s):
    '''this functions returns True. It is checking if 'c' 
    (a constant lower case string)
    is lower
    '''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
def any_lowercase3(s):
    ''' checks if the last letter is lower case or not
    '''
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    ''' checks if the string contains any lower case letters.
    This is a correct funciton.
    '''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    '''checks whether all the letters are lower case
    '''
    for c in s:
        if not c.islower():
            return False
    return True
s='triaL'
print(any_lowercase1(s))
print(any_lowercase2(s))
print(any_lowercase3(s))
print(any_lowercase4(s))
print(any_lowercase5(s))