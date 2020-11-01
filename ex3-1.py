# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:08:05 2020

@author: Ouso
"""

#Ex3-1

def right_justify(s):
    ''' shift the string to the right such that it ends on the 70th column
    s: string to right justify
    '''
    print(' '*(70-len(s))+s)


                                                          