# # map()
# def n22(n):
#     if type(n) in (int, float):
#         return n ** 2
#     else:
#         return 'Error: type error'
#
#
# number = [1, 2, 3, 4, 5]
# # for index in range(len(number)):
# #     number[index] = number[index] ** 2
# # print(number)
# number = map(n22, number)
# print(tuple(number))


# filter
def js(n):
    if n % 2 == 1:
        return n


number = [1, 2, 2, 2, 4, 6, 8, 9]
# n01 = []
# for i in number:
#     a = js(i)
#     n01.append(a)
# print(n01)
a = filter(js, number)
print(list(a))


# reduce
from functools import reduce
def n22(n, m):
    return n + m


number = [1, 2, 3]  # 2 ==>> 6
result = reduce(n22, range(1, 11))
print(result)

# 匿名函数(y=ax+b)
a = lambda x: 3 * x + 4
x = 5
y = a(x)
print(y)

def xyl(x):
    return 3 * x + 4

# sorted()
ips = {'1.1.1.1': 834, '2.2.2.2': 10024, '3.3.3.3': 15, '4.4.4.4': 1200}
result = sorted(ips.items(), key=lambda x: x[1], reverse=True)
print(dict(result))