# 在Python中为了让程序能够得到精简,我们回去引入函数的概念

# number = [1, 4, 2, 3, 5, 1]
# for i in range(len(number)):
#     for j in range(len(number) - 1):
#         if number[j] > number[j+1]:
#             number[j], number[j+1] = number[j+1], number[j]
#
#
# number02 = [23, 12, 34, 115, 123]
# for i in range(len(number)):
#     for j in range(len(number) - 1):
#         if number[j] > number[j+1]:
#             number[j], number[j+1] = number[j+1], number[j]

# 函数的定义
def funcName(param):
    pass

def mp(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print(l)

mp([12, 10, 45, 23, 31, 21])
number = [12, 11, 23, 21, 45, 34, 25]
mp(number)
