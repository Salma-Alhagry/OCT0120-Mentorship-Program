# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 02:47:22 2020

@author: Ouso
"""

'''
Exercise 12-1.
Write a function called most_frequent that takes a string and prints 
the letters in decreasing order of frequency. Find text samples from several 
different languages and see how letter frequency varies between languages. 
Compare your  results with the tables at
http://en.wikipedia.org/wiki/Letter_frequencies.
'''

def most_frequent(s):
    frequency =[]
    letters = list(s.lower())
    for i in letters:
        if i not in [ j[0] for j in frequency]:
            frequency.append((i,letters.count(i)))
    frequency.sort(key= lambda x: x[1],reverse=True)
        
    return frequency
def most_frequent2(s):
    frequency ={}
    