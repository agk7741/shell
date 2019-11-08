# # 求一个数的平方或立方或4次方
# def aaa(m=2):
#     def bbb(n=1):
#         result = n ** m
#         return result
#     return bbb
#
# # 求2的8次方
# jsq = aaa(8)
# number = jsq(2)
# number = jsq(3)
# print(number)

# def sums(a, b):
#     return a + b
#
# opera = sums
# print(opera)
# print(sums(1, 2))
# print(opera(1, 2))


# 计步器: 默认从0步开始计步, 如果用户需要修改自己的步数也可以支持修改
def bs(step=1):
    def addr():
        nonlocal step
        step += 1
        return step
    return addr


jbq = bs()
bushu = jbq()
print(bushu)
bushu = jbq()
print(bushu)
bushu = jbq()
print(bushu)

jbq = bs(4)
bushu = jbq()
print(bushu)
bushu = jbq()
print(bushu)
bushu = jbq()
print(bushu)


