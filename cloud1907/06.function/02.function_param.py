# 函数的参数问题
# 求一个数的绝对值
# y = |x|
# number = int(input('please input number: '))
# if number < 0:
#     number = -number
#     print(number)
# else:
#     print(number)

def abc(number):
    if number < 0:
        number = -number
        print(number)
    else:
        print(number)


def abs(param01, param02, param03, param04):
    param05 = 10
    print(param01 + param02 + param03 + param04 + param05)


def abd(param01=0, param02=0):
    print(param01 + param02)


abd(param02=78)

