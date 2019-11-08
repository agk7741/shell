# for i in range(6, 11):
#     pass
#
# n = 0
# while n < 100:
#     pass
#     n += 1
#
# while True:
#     pass

# break: 跳出循环,并不是跳过本次子循环---终止循环
# continue: 跳过循环,中止子循环
for i in range(1, 101):
    if i % 2 == 0:
        continue
    print(i)

