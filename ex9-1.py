# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:53:07 2020

@author: Ouso
"""

'''
Exercise 9-1.
Write a program that reads words.txt and prints only the words with 
more than 20 characters (not counting whitespace).
'''
f= input('insert file name.ext')
def words_bigger_20(f):
    fin = open(f)
    word=''
    for line in fin:
        word=fin.readline().strip()
        if len(word) >20:
            print(word)
words_bigger_20(f)

#answer is :
#counterdemonstrations