# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 08:25:52 2020

@author: Ouso
"""

'''
Exercise 15-1.
Write a definition for a class named Circle with attributes center and radius, where
center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at
150, 100
 and
radius 75.
Write a function named point_in_circle that takes a Circle and a Point and returns
True if the Point lies in or on the boundary of the circle.
Write a function named rect_in_circle that takes a Circle and a Rectangle and
returns True if the Rectangle lies entirely in or on the boundary of the circle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle
and returns True if any of the corners of the Rectangle fall inside the circle. Or as a
more challenging version, return True if any part of the Rectangle falls inside the
circle.
'''
class Point:
    '''defines a point with x and y coordinates'''
class Circle:
    '''define circle with attributes center and radius
    center is a point object
    radius is a number
    '''
class Rectangle:
    '''rectangle defined with a corner and width and height'''
circle = Circle()
circle.radius = 75
circle.center = Point()
circle.center.x=150
circle.center.y=100

def point_in_circle(p,circ):
    return (circ.center.x -circ.radius<=p.x <= circ.center.x +circ.radius)and\
            (circ.center.y -circ.radius<=p.y <= circ.center.y +circ.radius)
p=Point()
p.x=74
p.y=100
print(point_in_circle(p,circle))

def rect_in_circle(rect, circ):
    return (point_in_circle(rect.corner,circ)) and (point_in_circle(rect.p2,circ))\
             and (point_in_circle(rect.p3,circ)) and (point_in_circle(rect.p4,circ))
def rect_circle_overlap(rect,circ):
    '''finds whether rect overlaps with circle, this code is not complete
    and fails in cases where the rectangle contains the full circle'''
    return (point_in_circle(rect.corner,circ)) or (point_in_circle(rect.p2,circ))\
             or (point_in_circle(rect.p3,circ)) or (point_in_circle(rect.p4,circ))
def rect_circle_overlap_gen(rect,circ):
    ''' finds whether rect overlaps with circle including the case of full
    circle inside the rectngle'''
    return ((rect.corner.x <circ.center.x -circ.radius) and (rect.p3.x <circ.center.x -circ.radius))\
            or ((rect.corner.x <circ.center.x +circ.radius) and (rect.p3.x <circ.center.x +circ.radius))\
            or ((rect.corner.y <circ.center.y -circ.radius) and (rect.p3.y <circ.center.y -circ.radius))\
            or ((rect.corner.y <circ.center.y +circ.radius) and (rect.p3.y <circ.center.y +circ.radius))
rect = Rectangle()
rect.width = 300
rect.height =400
rect.corner= Point()
rect.corner.x = 50
rect.corner.y= 20
rect.p2= Point()
rect.p2.x = rect.corner.x
rect.p2.y= rect.corner.y+ rect.height
rect.p3= Point()
rect.p3.x = rect.corner.x+ rect.width
rect.p3.y= rect.corner.y
rect.p4= Point()
rect.p4.x = rect.corner.x+ rect.width
rect.p4.y= rect.corner.y+ rect.height
print(rect_in_circle(rect, circle))
print(rect_circle_overlap(rect, circle))
print(rect_circle_overlap_gen(rect, circle))