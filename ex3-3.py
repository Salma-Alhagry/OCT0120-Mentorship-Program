# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 01:53:12 2020

@author: Ouso
"""
def do_twice(f,*arg):
    f(*arg)
    f(*arg)
def do_four(f,*arg):
    do_twice(f,*arg)
    do_twice(f,*arg)
def draw_grid_line(*arg):
    print(*arg)
print('+'+'-'*4+'+'+'-'*4+'+')
do_four(print,'|'+' '*4+'|'+' '*4+'|')
print('+'+'-'*4+'+'+'-'*4+'+')
do_four(print,'|'+' '*4+'|'+' '*4+'|')
print('+'+'-'*4+'+'+'-'*4+'+')