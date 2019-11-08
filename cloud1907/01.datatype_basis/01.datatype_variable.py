# 如何使用Python输出hello world
print("hello world")


# 整型 = int
print(1)
print(type(1))

# 浮点型 = float
print(3.14)
print(type(3.14))

# 字符串类型 = str
print("hello world")
print(type("hello world"))

# 布尔值类型 = bool
print(True)
print(False)
print(type(True))
print(type(False))

# 数据类型转换
print(type(3.64))
# 强制把3.14转换为整型
print(int(3.64))

# 强制把字符串类型转换为整型或浮点型
print(type('1'), type('3.14'))
print(int('1'), type(int('1')))
print(float('3.14'), type(float('3.14')))

# 强制把整型及浮点型转化为字符串类型
print(type(1), type(3.14))
print(str(1), type(str(1)))


# 转化布尔值类型为整型,反之亦然
print(bool(1))
print(int(True))

# 三引号的字符串声明方式
print('''this is my house
this first line
222222222222222
333333333333333''')
