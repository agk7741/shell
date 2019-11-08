# 条件判断
number = int(input('please input intial: '))
if number > 0:
    print('number > 0 is true!')
elif number < 0:
    print('number < 0 is true!')
else:
    print('number == 0 is true!')


# 找出1-10里既能被3整除又能被2整除的数字
if number % 3 == 0:
    if number % 2 == 0:
        print(number)

# for: 爱因斯坦阶梯
for ladder in range(7, 200):
    if ladder % 2 == 1:
        if ladder % 3 == 2:
            if ladder % 4 == 3 and ladder % 5 == 4:
                if ladder % 6 == 5 and ladder % 7 == 0:
                    print(ladder)

# while: 死循环
n = 1
while n <= 100:
    if n % 2 == 0:
        print(n)
    n += 1



