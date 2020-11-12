# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:29:22 2020

@author: Ouso
"""
'''
Exercise 19-1.
The following is a function that computes the binomial coefficient recursively:
def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """
    memo = {(0,0):1, (0,1):0}
    if (n,k) in memo:
        return memo[(n,k)]
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    memo[(n,k)] = res
    return res
Rewrite the body of the function using nested conditional expressions.
One note: this function is not very efficient because it ends up computing the same
values over and over. You could make it more efficient by memoizing (see “Memos”
on page 131). But you will find that it’s harder to memoize if you write it using condi‐
tional expressions.
'''
def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".
    n: number of trials
    k: number of successes
    returns: int
    """

    return 1 if k==0 else 0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)

def binom2(n,k):
    memo = {(0,0):1, (0,1):0}
    if (n,k) in memo:
        return memo[(n,k)]
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    memo[(n,k)] = res
    return res

def binom3(n,k):
     memo = {(0,0):1, (0,1):0}
     print(memo)
     return memo[(n,k)] if (n,k) in memo else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)