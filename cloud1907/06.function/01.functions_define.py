#!/usr/bin/env python3
# coding: utf8
#
# author: bavdu
# date: 2019/08/05
# usage: functions define


def funcName(a, b):
    """
    define sum function
    :param a: type: int
    :param b: type: int
    :return: a+b
    """
    s = a + b
    return s


# help(funcName)
# 函数的调用
print(funcName(1, 2))
log = funcName(1, 3)


def maxNum(a, b, c):
  number = [a, b, c]
  m = number[0]
  for n in number:
    if m < n:
      m, n = n, m
  return m, n


x, y = maxNum(1, 2, 3)
print(x, y)