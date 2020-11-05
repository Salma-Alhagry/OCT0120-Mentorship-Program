# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 02:45:39 2020

@author: Ouso
"""

'''
Exercise 11-3.
Memoize the Ackermann function from Exercise 6-2 and see if memoization 
makes it possible to evaluate the function with bigger arguments. Hint: no.
'''
known_ack={(0,0):1,(0,1):2}

def ack(m,n):
    
    if (m,n) in known_ack:
        return known_ack[(m,n)]
    
    if m ==0:
        ack_calc = n+1
        known_ack[(m,n)] = ack_calc
        return ack_calc
    
    elif m>0 and n ==0:
        ack_calc = ack(m-1, 1)
        known_ack[(m,n)] = ack_calc
        return ack_calc
    
    elif m >0 and n>0:
        ack_calc = ack(m-1, ack(m,n-1))
        known_ack[(m,n)] = ack_calc
        return ack_calc
        
print(ack(3,10))
print('''
      The function causes runtime error when m > 3 and/or n>10
      ''')
