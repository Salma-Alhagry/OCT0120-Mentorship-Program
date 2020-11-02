# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:18:52 2020

@author: Ouso
"""

'''
Exercise 6-1.
Draw a stack diagram for the following program. What does the program print?
'''
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))


print('''

      __main__:
      
      x --> 1
      y --> 2
      
      
      c:
      x --> 1
      y --> 5
      z --> 3
      total --> 9
      square -->  8100  <--  
                          |
                          |        
      b:                  |
      z --> 9  ------------
      prod --> 90<-     |
                  |     |
                  |     |
      a:          |     |
          x-->9   |
          x--> 10--  <---  
          y --> 9
    
      
 The program prints:
9 90
8100     
      
      ''')