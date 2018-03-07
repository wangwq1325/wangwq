#!/usr/bin/env python
#-*- coding:utf-8 -*-

#命名关键字参数
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print ('name:',name,'age:',age,'other:',kw)

person('jack',24,city = 'Beijing',addr = 'chaoyang',zipcode=123456)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符"*"，
#"*"后面的参数被视为命名关键字参数
#def person(name,age,*,city,job):
#    print(name, age, city, job)

#person('jack',24,city='Beijing',job='Engineer')

def person(name,age,*args,city,job):
    print(name,age,args,city,job)

person('Jack',24,'Beijing','Engineer')

