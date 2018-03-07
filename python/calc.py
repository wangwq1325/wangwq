#!/usr/bin/env python
#-*- coding:utf-8 -*-

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum

result = calc([1,2,3])
print "result= ",result
result = calc((1,3,5,7))
print "result= ",result


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum

result = calc(1,2,3)
print "result1= ",result
result = calc(1,3,5,7)
print "result1= ",result

nums = [1,2,4]
result = calc(nums[0],nums[1],nums[2])
print "result2= ",result


