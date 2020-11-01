# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:39:18 2020

@author: Ouso
"""
#ex2-1
print('Ex 2-1 \n')

''' Repeating my advice from the previous chapter, whenever you learn a new feature,
you should try it out in interactive mode and make errors on purpose to see what
goes wrong.''' 

# We’ve seen that n = 42 is legal. What about 42 = n?

print ('42=n returns SyntaxError: can\'t assign to literal \n' )

#How about x = y = 1?

print('this works and returns nothing, the assignment statement is correct \n')

'''in some languages every statement ends with a semicolon, ;. What happens if
you put a semicolon at the end of a Python statement?'''
print('nothing happens \n')

#What if you put a period at the end of a statement?
''' In math notation you can multiply x and y like this: xy
. What happens if you try that in Python?'''
print('in most of the cases it will generate syntax error, SyntaxError: '
      "invalid syntax \n ")
