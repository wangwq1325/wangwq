#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Returns the value of the quadratic equation with one unknown
#ax^2+bx+c = 0

import math

def quadratic(a,b,c):
    if a == 0:
        print "this is not two order equation"
        return
    else:
        r = math.sqrt(b*b-4*a*c)
        x1 = (-b-r)/(2*a)
        x2 = (-b+r)/(2*a)
        return x1,x2
x = quadratic(1,3,-4)
print x

