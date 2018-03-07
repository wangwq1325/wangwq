#!/usr/bin/env python
#-*- coding:utf-8 -*-

def fact(n):
    if n== 1:
        return n
    else:
        return n*fact(n-1)

print '5!= ',fact(5)
print '1!= ',fact(1)
#print "100!=",fact(100)溢出

