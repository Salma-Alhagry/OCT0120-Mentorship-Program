# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 01:32:37 2020

@author: Ouso
"""

'''
Exercise 7-3.
The mathematician Srinivasa Ramanujan found an infinite series that can be 
used to generate a numerical approximation of 1/π

Write a function called estimate_pi tha t uses this formula to compute 
and return an estimate of π. It should use a while loop to compute terms of the 
summation until the last term is smaller than 1e-15 
'''
import math

def estimate_pi():
    k=0
    summation_const = 2*math.sqrt(2)/9801
    pi_eval = 1
    pi_inv = 0
    while abs(math.pi-pi_eval) >= 1e-15:
        pi_inv += (math.factorial(4*k)*(1103 + 26390*k))/\
        ((math.factorial(k)**4)*(396**(4*k)))
        pi_eval = 1/(summation_const*pi_inv)
        k+=1
        print(pi_eval, k)
    return pi_eval, math.pi

print(estimate_pi())