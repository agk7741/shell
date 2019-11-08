# 函数
# def sums(a, b):
#     s = a + b
#     return s


# result = sums(12, 13)
# print(result)

# def sums(a):
#     def wrapper(b):
#         s = a + b
#         return s
#     return wrapper
#
#
# jsq = sums(8)
# result = jsq(13)
# print(result)

# # 求1~100的和
# def qh(n):
#     if n == 1:
#         return n
#     return qh(n - 1) + n
#
#
# # 求1~10的阶乘
# def ladder(n):
#     if n == 1:
#         return n
#     return ladder(n - 1) * n


xy = lambda x, y: x ** 2 + y
print(xy(2, 1))

# map,reduce,filter,sorted
def ou(element):
    if element % 2 == 0:
        return element


slist = [1, 2, 3, 4, 5, 6]
result = filter(ou, slist)
print(list(result))


def q2(n):
    return n ** 3


q3 = lambda n: n ** 3
slist = [1, 2, 3, 4]
print(list(map(q3, slist)))


from functools import reduce
# def add(x, y):
#     return x + y


add = lambda x, y: x + y
slist = [1, 2, 3, 4, 5]
result = reduce(add, slist)
print(result)




