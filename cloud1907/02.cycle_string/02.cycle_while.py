# while循环框架
# n = 0
# while n < 100:
#     print(n)
#     n += 1

# while死循环
# while True:
#     print("hello world")

# break跳出循环体
# n = 0
# while True:
#     if n == 0:
#         print("hello world")
#         break

# 1~100:
n = 0
while n <= 99:
    n += 1
    if n % 2 == 1:
        continue    # 跳过本次循环体
    print(n)

