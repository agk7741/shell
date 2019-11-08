# 整型, 浮点型, 字符串类型, 布尔值类型
# 整型涉及到的应用案例
# 加减乘除,取余,除后取整
# 取1~100中所有的偶数
# for n in range(1, 101):
#     if n % 2 == 0:
#         print(n)
#
# n = 0
# while n < 100:
#     n += 1
#     if n % 2 == 0:
#         print(n)
#
# while True:
#     break: 当满足某个条件时, 整体循环直接退出
#     continue: 当满足某个条件时,程序将会退出本次循环, 继续下一次循环
# for n in range(1, 101):
#     if n % 2 == 1:
#         continue
#     print(n)

# for i in range(1, 100):
#     for j in range(1, 10):
#         if i + j == 2:
#             break
#     print("{} break not run!".format(i))

# 字符串类型
# string = """"""
# string = 'hello world'
# for index in range(len(string)):
#     print(string[index])
#
# for word in string:
#     print(word)

# with open(file='mysql_password', mode='r') as file:
#     for lines in file.readlines():
#         if 'password' in lines:
#             print(lines.split()[1])
#             break

def getPswd(filename):
    with open(file=filename, mode='r') as files:
        for lines in files.readlines():
            if 'password' in lines:
                return lines.split()[1]


string = 'hello world'
print(string[5:])
print(string[-11:-6])













