
# 如何间接更改元组中的元素
list01 = [1, 2, 3, 4, 5]
# tuple01 = (1, 2, 3, 4, list01)
tuple01 = (1, 2, 3, 4, [1, 2, 3, 4, 5])
# print(type(tuple01))
tuple01[-1][3] = 'c'
print(tuple01)

# 元组中的方法
# index, count
# 元组中是支持索引, 可以支持元素的查找, 也可以支持遍历元组
t01 = (1, 2, 3, 4, 5)
print(t01[1:3])

for i in range(len(t01)):
    if t01[i] % 2 == 0:
        print(t01[i])

# 遍历元组: 迭代: 利用for循环可以直接对元组或列表中的元素进行提取, 而不是用索引将其输出
for element in tuple01:
    print(element)

# 遍历列表: 迭代:
list01 = [1, 2, 3, 4, 5]
for element in list01:
    print(element)


# 对于列表于元组而言，是可以相互转换的
# int -->> float
# int -->> str
# int(1/0) -->> (True/False)
number = [1, 2, 3, 4, 5, 6]
charset = ('tom', 'jerry', 'hale')
print(type(number))
print(type(charset))

# number转化为元组类型
number_change = tuple(number)
print(number_change, type(number_change))
# charset转化为列表
charset_change = list(charset)
print(charset_change, type(charset_change))

