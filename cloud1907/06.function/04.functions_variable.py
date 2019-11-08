#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: functions param


# 全局变量及局部变量
variable = 1
def funcName(param=0):
    global variable
    variable = 78
    s = param + variable
    return s

result = funcName(4)
print(result)
print(variable)


# nonlocal变量
def waibu():
    x = 12
    def neibu():
        print(x)
    print(x)
    neibu()




def waibuh():
    x = 90
    def neibuh():
        nonlocal x
        x = 28
        print(x)
    neibuh()
    print(x)

waibuh()













