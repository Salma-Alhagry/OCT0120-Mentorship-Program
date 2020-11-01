# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:15:49 2020

@author: Ouso
"""
#ex1-2
'''
Start the Python interpreter and use it as a calculator.

1. How many seconds are there in 42 minutes 42 seconds?'''
print('Ans 1. There are ', 42*60+42, ' seconds \n')

'''2. How many miles are there in 10 kilometers? Hint: there
      are 1.61 kilometers in a mile.'''
print('Ans 2. There are ',10/1.61, ' miles in km \n')

'''3. If you run a 10 kilometer race in 42 minutes 42 seconds,
      what is your average pace (time per mile in minutes and seconds)?
      What is your average speed in miles per hour? '''
print('Ans 3. The pace in min/ mile is ',(42+(42/60))/(10/1.61),
      'min/mile',' and the pace in sec/mile is ',
      (42*60+42)/(10/1.61),'sec/mile')

print('The average speed in mile per hour is ',
      (10/1.61)/((42+(42/60))/60),'mile/hour')