# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 02:13:13 2020

@author: Ouso
"""

def print_twice(*arg, end=''):
    print(*arg,end)
    print(*arg)
def print_four(*arg,end=''):
    print_twice(*arg, end)
    print_twice(*arg)
def draw_grid_line(*arg):
    print(*arg)

print_twice(draw_grid_line,'+','-'*4, end=' ')