# 整型、浮点型、字符串类型、布尔值类型
# 变量: 在内存中开辟一段空间,把该空间的地址链接到变量名上
# 然后利用变量的名字把对应的值放入到内存空间中的过程就是变量赋值的过程

number = 314
floatA, strA = 3.84, 'hello'
boolA, boolB = True, False

# 整型、浮点型的四则运算和取余与取整
print(number + 10)
print("number + 10 = {}".format(number + 10))
print("number / 3 = {}".format(number / 3))
print("number % 3 = {}".format(number % 3))
print("number // 3 = {}".format(number // 3))
print("floatA % 3 = {}".format(floatA % 3))
print("floatA // 3 = {}".format(floatA // 3))
# 整型与浮点型之间的类型转换int() // float()
print(float(number))
print(int(floatA))
# 整型与浮点型 和 字符串类型 之间的转换
# print(int(strA)) 这种操作是不被允许的
strB = '123.3'
# print(int(strB))
print(float(strB))

# list type change to str
listA = [1, 2, 3, 4, 5]
number = str(listA)
print(number, type(number))

# 字符串的计算
print(strB * 10)
print(strB + 'abc')

# and // or // not
print(True and True)
print(True or False)
print(not True)

