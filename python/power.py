#!/usr/bin/env python
#-*- coding:utf-8 -*-

#def power(x):
#   return x*x
#计算x的n次幂
def power(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print power(2,6),power(2)



