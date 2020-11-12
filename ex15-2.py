# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:29:46 2020

@author: Ouso
"""

'''
Write a function called draw_rect that takes a Turtle object and a Rectangle and uses
the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.
Write a function called draw_circle that takes a Turtle and a Circle and draws the
Circle.
'''
import turtle
import draw ## contains authors functions for drawing rectangles and circles

class Point:
    '''define a point with x,y coordinates'''

class Rectangle:
    '''define rectangle using corner and width and height'''
class Circle:
    '''defines a circle using a center point and radius value'''

rect = Rectangle()
rect.width = 100
rect.height=150
rect.corner = Point()
rect.corner.x=10
rect.corner.y=10
circ = Circle()
circ.r= 13

def shift_center(turtle,distance):
    ''' function to draw from origin of circle'''
    turtle.pu()
    turtle.fd(distance)
    turtle.lt(90)
    turtle.pd()
    
def shift_corner(turtleobj, x, y):
    '''funciton to move the point of drawing of rectangle objects to the any 
    corner point'''
    turtleobj.pu()
    turtleobj.fd(x)
    turtleobj.lt(90)
    turtleobj.fd(y)
    turtleobj.lt(270)
    turtleobj.pd()

        
    
    
def draw_rect(rect):
    turtleobj = turtle.Turtle()
    shift_corner(turtleobj,rect.corner.x,rect.corner.y)

    for i in range(2):
        turtleobj.fd(rect.width)
        turtleobj.lt(90)
        turtleobj.fd(rect.height)
        turtleobj.lt(90)
print(draw_rect(rect))
    
def draw_circle(circle):
    turtleobj = turtle.Turtle()
    shift_center(turtleobj,circle.r)
    draw.circle(turtleobj,circle.r)
    
print(draw_circle(circ))
    
    
    

