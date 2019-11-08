# 不定长度参数: *args
# def sums(*args):
#     s = 0
#     for element in args:
#         s += element
#     return s


# def sums01(a, b, c, d, e, f, g, h, i, j):
#     return a+b+c+d+e+f+g+h+i+j
# result = sums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(result)


# Python中函数的多态
def sums(a, b):
    return a + b


print(sums(1, 2))
print(sums(3.14, 4.445))
print(sums(1, 3.14))
print(sums('abc', 'def'))
print(sums([1, 2, 3], [4, 5, 6, 7]))
print(sums((1, 2, 3), (4, 5, 6)))
# print(sums({1, 2, 3}, {4, 5, 6}))
# print(sums({'name': 'tom'}, {'age': 18}))


# 任意类型的参数
def sums(*args, **kwargs):
    # args: 不定长度,所产生的数据类型为: 元组(tuple)
    # kwargs: 不定类型,所产生的数据类型为: 字典(dict)
    for items in kwargs.items():
        print(items)


# 函数参数的作用域01
number = 119        # 全局变量
def suns(a, b):
    return a + b + number

# print(a, b)

print(suns(1, 1))
# 函数参数的作用域02
number02 = 119
def suns(a, b):
    number03 = 10   # 局部变量
    return a + b + number02 + number03


print(suns(1, 1))
# print(number03)
# 函数参数的作用域03
# number04 = 68
def suns(a, b):
    global number04
    number04 = 45
    return a + b + number04

print(suns(1, 1))
print(number04)






