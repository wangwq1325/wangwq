#!/usr/bin/env python
#-*- coding:utf-8 -*-
#关键字参数
def person(name,age, **kw):
    print ('name:',name,'age:',age,'other:',kw)

person('Michael',30)

person('Bob',35,city='Beijing')

person('Adam',45,gender='M',job='engineer')

extra = {'city':'Beijing','job':'Engineer'}
person('jack',24,city=extra['city'],job=extra['job'])
person('jack',24,**extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入
#到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra
#的一份拷贝，对kw的改动不会影响到函数外的extra

def person(name,age,*,city,job):
    print(name,age,city,job)
person ('Jack',24,'Beijing','Engineer')
