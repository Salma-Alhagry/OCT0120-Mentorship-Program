# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 08:27:41 2020

@author: Ouso
"""

'''
Exercise 17-2.
This exercise is a cautionary tale about one of the most common, and difficult to find,
errors in Python. Write a definition for a class named Kangaroo with the following
methods:
1.
An __init__ method that initializes an attribute named pouch_contents to an
empty list.
2.
A method named put_in_pouch that takes an object of any type and adds it to
pouch_contents.
3. A __str__ method that returns a string representation of the Kangaroo object
and the contents of the pouch.
'''

class Kangaroo:
    def __init__(self):
        self.pouch_contents = []
    def put_in_pouch(self,obj):
        
        self.pouch_contents.append(obj)
    def __str__(self):
        content = ''
        for obj in self.put_in_pouch:
            content += ' '.join(str(obj))
        return 'Kangaroo objects are: '+content
            