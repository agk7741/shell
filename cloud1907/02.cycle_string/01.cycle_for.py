# for循环的框架
# for i in range(100):
#     print(i)

# 找出1~100之间的偶数
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# 找出1~100之间的奇数
# for i in range(1, 101):
#     if i % 2 == 1:
#         print(i)

# 利用for循环来遍历字符串
string = "this is my house"
# for i in string:
#     print(i)

# 判断『s』是否存在于string字符串中
for i in string:
    if i == 's':
        print('含有')

# 一个人走楼梯, 每次上2阶最后会剩下一阶；
# 如果每次上3阶最后会剩下两阶；
# 如果每次上4阶最后会剩下三阶；
# 如果每次上5阶最后会剩下四阶；
# 如果每次上6阶最后会剩下五阶;
# 如果每次上7阶正好可以走完;
# 问这个楼梯最短的阶数；
for ladder in range(7, 10000):
    if ladder % 2 == 1 and ladder % 3 == 2 and ladder % 4 == 3 and ladder % 5 == 4 and ladder % 6 == 5:
        if ladder % 7 == 0:
            print(ladder)


