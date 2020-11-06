# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:34:41 2020

@author: Ouso
"""

'''
Exercise 5-2.
Fermat’s Last Theorem says that there are no positive integers a, b, and c 
such that

a^n + b^n = c^n

for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters—a, b, c and n
—and checks to see if Fermat’s theorem holds. If n is greater than 2 and

a^n + b^n = c^n

the program should print, “Holy smokes, Fermat was wrong!” Otherwise the pro‐
gram should print, “No, that doesn’t work.”

2. Write a function that prompts the user to input values for a, b, c and n, 
converts them to integers, and uses check_fermat to check whether they violate
Fermat’s theorem.
'''


def check_fermat(a , b, c, n):
    ''' a function to check if 3 positive integers a,b,c satsify Fermat's 
    theroem when raised to power n >2 and do not satisfy the form
    
    a^n + b^n = c^n
    
    a,b,c: positive integers
    
    n: integer > 2
    
    '''

    if a == abs(a) and b==abs(b) and c==abs(c) and n>2:
        
        if a**n+b**n==c**n :
            print("Holy smokes, Fermat was wrong!")
        
        else:
            print("No, that doesn’t work.")
    else:
        print('rerun function, one of a, b, and c is negative or n <=2')

def prove_fermat_wrong():
    ''' 
    input the 4 values of a, b ,c, and n to check Fermat's theorem
    '''
    a = int (input('input a positive integer \n'))
    b = int (input('input a positive integer \n'))
    c = int (input('input a positive integer \n'))
    n = int (input('input an integer >2 \n'))
    
    check_fermat(a , b, c, n)

prove_fermat_wrong()