#!/usr/bin/env python
#-*- coding:utf-8 -*-

def findMinMax(*L):
        for i in L:
             minnum = min(L)
             maxnum = max(L)
        return (minnum,maxnum)

x = findMinMax(1,2,3,4,6)
print x
