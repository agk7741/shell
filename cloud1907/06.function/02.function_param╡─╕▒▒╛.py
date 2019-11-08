#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: functions param


# 赋予参数默认值
def add(a=0, b=0):
    """
    sum
    :param a: int
    :param b: int
    :return: a+b
    """
    s = a + b
    return s


print(add(1, 3))


# 多态
var01 = "hello"
var02 = "world"
print(var01 + var02)
print(add(var01, var02))

list01 = [1, 2, 3, 4]
list02 = [5, 6, 7, 8]
print(add(list01, list02))


# 多参数传入
def add(*args, **kwargs):
    for element in args:
        print(element)
    for dicts in kwargs.items():
        print(dicts)


# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, [18, 13], {45: 31, 81: 90}, {1, 2, 3, 4}, bavduer='key'))
add(1, 2, 3, 34, 5, 6, 7, 8)
add(1, 2, 3, bavduer=34, opera=34, kkk=23)


