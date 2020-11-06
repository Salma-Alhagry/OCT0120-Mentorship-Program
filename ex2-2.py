# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 01:03:59 2020

@author: Ouso
"""

print( '\n Ex 2-1 \n' )

# problem 1 
r=5
pi = 3.14
print('Ans 1. radius = ', (4*pi*r**3)/3,'cm^3 \n')

# problem 2
num_books = 60
book_price =24.95
book_store_discount = 40/100
first_copy_ship_cost = 3
copy_ship = .75
total = num_books * book_price*book_store_discount + first_copy_ship_cost \
+ copy_ship*(num_books-1)

print('Ans 2. total cost= ',total, '\n' )

#problem 3
start_time_hr = 6
start_time_min = 52
easy_pace_min = 8
easy_pace_sec=15
tempo_pace_min = 7
tempo_pace_sec = 12

time_in_mins = 2*(easy_pace_min+(easy_pace_sec/60))+3*(tempo_pace_min+\
                tempo_pace_sec/60)
end_time_min=((52+time_in_mins)/60-int((52+time_in_mins)/60))*60
end_time_hr = int((52+time_in_mins)/60)+6
print('Ans 3. arrival time is ', end_time_hr,':',end_time_min)