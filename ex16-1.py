# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 00:36:13 2020

@author: Ouso
"""
'''
Exercise 16-1.
Write a function called mul_time that takes a Time object and a number and returns a
new Time object that contains the product of the original Time and the number.
Then use mul_time to write a function that takes a Time object that represents the
finishing time in a race, and a number that represents the distance, and returns a
Time object that represents the average pace (time per mile).
'''
class Time:
    ''' class of objects that describe time in hr:min:sec format'''

def mul_time(time, num):
    n_time=Time()
    n_time.sec = (time.sec * num)%60
    n_time.min = (time.min *num + time.sec*num//60)%60
    n_time.hr = (time.hr * num + time.min*num//60)
    return "%.2d:%.2d:%.2d" %(n_time.hr , n_time.min,n_time.sec)

time = Time()
time.sec = 30
time.min = 40
time.hr = 2
print(mul_time(time,2))

def avg_pace(fin_time,distance):
    time_per_dist = mul_time(fin_time, 1/distance)
    return time_per_dist, str(float(time_per_dist[0:2]) \
                              + float(time_per_dist[3:5])/60\
         + float(time_per_dist[7:9])/3600)+' hr/mile'