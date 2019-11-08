# 变量名 = <整型、浮点型、字符串类型、布尔值类型>
# 首先CPU把变量名对应到内存空间(内存地址)中，把3.14存储到对应的内存空间中
var01 = 3.14
var02 = 1

print(var01, var02)
print(var01, type(var01))
print(var02, type(var02))


# 链式赋值
var03 = var04 = var05 = 0
# 分别赋值
var06, var07 = 1, 2
var08, var09, var10 = 0, 0, 0

# 把下面两个变量进行交换
n01 = "hello"
n02 = "world"
print(n01, n02)
# step01: other variable
n03 = n01
n01 = n02
n02 = n03
print(n01, n02)
print(n03)
# step02: change variable local
n01, n02 = n02, n01
print(n01, n02)
print(n03)

