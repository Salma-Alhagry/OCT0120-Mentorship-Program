# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 01:29:01 2020

@author: Ouso
"""
'''Exercise 16-2.
The datetime module provides time objects that are similar to the Time objects in
this chapter, but they provide a rich set of methods and operators. Read the docu‐
mentation at http://docs.python.org/3/library/datetime.html.
1.
Use the datetime module to write a program that gets the current date and prints
the day of the week.
2.
Write a program that takes a birthday as input and prints the user’s age and the
number of days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as
the other. That’s their Double Day. Write a program that takes two birthdays and
computes their Double Day.
4.
For a little more challenge, write the more general version that computes the day
when one person is n times older than the other.
'''
import datetime


def get_day_of_week():
    '''gets current date and returns the day of the week'''
    days=['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday','Sunday']  
    return days[datetime.weekday(datetime.datetime.today())]

def Bday_age():
    '''gets birthday and returns age'''
    bday_user=input('insert birthday yyyy-mm-dd: \n')
    bday = datetime.datetime.strptime(bday_user,'%Y-%m-%d')
    today=datetime.datetime.today()
    age = (today-bday).days/365.25
    return age
    
def double_day():
    '''asks user for 2 birthdates and return the day one of them is twice 
    the age of the other'''
    bd1 =input('insert birthday yyyy-mm-dd: \n')
    bd2=input('insert birthday yyyy-mm-dd: \n')
    bd1=datetime.datetime.strptime(bd1, "%Y-%m-%d")
    bd2=datetime.datetime.strptime(bd2, "%Y-%m-%d")
    if bd1<bd2:
      
        double_date = bd2-(bd1-bd2)
    else:
        double_date = bd1-(bd2-bd1)

    return double_date

def n_day(bd1,bd2,n):
    '''asks user for 2 birthdates and return the day one of them is n times 
    the age of the other'''
    bd1=datetime.datetime.strptime(bd1, "%Y-%m-%d")
    bd2=datetime.datetime.strptime(bd2, "%Y-%m-%d")
    
    if bd1<bd2:
        base = bd2-(bd1-bd2)
    else:
        base = bd1-(bd2-bd1)
    date = bd2 - base
    date = bd2 - date/(n-1)
        
        
    
    return date