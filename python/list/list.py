#!/usr/bin/env python
#-*- coding:utf-8 -*-

list = list(range(1,11))
print list

L = []
for x in range(1,11):
    L.append(x*x)
print L

L = [x*x for x in range(1,11)]
print L

g = (x*x for x in range(1,11))

for i in g:
    print i

#斐波拉契数列（Fibonacci）

def fib(max):
    n,a, b, = 0,0,1
    while n< max:
        print (b)
        a,b = b, a+b
        n = n+1
    return 'done'
print fib(8)

def fib(max):
    n,a, b, = 0,0,1
    while n< max:
        yield b
        a,b = b, a+b
        n = n+1

for n in fib(8):
    print (n)
