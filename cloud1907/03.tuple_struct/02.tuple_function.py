# # 元组中自带的一些方法
# t01 = (1, 2, 3, 4, 5)
#
# # 找出对应元素的索引
# index = t01.index(3)
# print(index)
#
# # 找到元组中元素索引的位置
# search = int(input('please input your search: '))
# if search in t01:
#     print("{}'s index: {}".format(search, t01.index(search)))
# else:
#     print("{} not exist of t01.".format(search))
#
# # 在指定区间查找元素的索引值
# t02 = (1, 2, 3, 4, 5, 1, 2, 3)
# print(t02.index(1, 1, len(t02)-1))
#
# # 统计元组中特定元素的个数
# t03 = (1, 2, 1, 3, 4, 5, 1, 2, 3, 4, 5)
# number = t03.count(1)
# print(number)
#
# # 元组之间的比较（局限性较大）
# t04 = (12, 7)
# t05 = (11, 5)
# if t04 > t05:
#     print(True)
# else:
#     print(False)
#
# list01 = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
# for i in range(len(list01)):
#     for j in range(len(list01) - 1):
#         if list01[j] > list01[j+1]:
#             list01[j], list01[j+1] = list01[j+1], list01[j]
# print(list01)
import sys
number = [11, 12, 15, 21, 23, 24, 29, 45, 57, 80, 99]
search = int(input("please input your search: "))
if search not in number:
    print('{} is not in number list.'.format(search))
    sys.exit()
start, stop = 0, len(number)
while stop - start > 0:
    middle = (start + stop) // 2
    if search < number[middle]:
        stop = middle
    elif search > number[middle]:
        start = middle
    else:
        print(number.index(search))
        break

