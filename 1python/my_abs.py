#!/usr/bin/env python
#-*- coding:utf-8 -*-

#*Limited data types*
def my1_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x > 0:
        return x
    else:
        return -x
#Use the empty function
def nop():
    if age >= 18:
        pass
a = -10.8
print "a = ",my1_abs(a)

#Return multiple values

import math

def move(x,y,step,angle = 0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx ,ny
x,y=move(100,100,60,math.pi/6)
print "1: ",x,  y
r=move(100,100,60,math.pi/6)
print "2: ",r
