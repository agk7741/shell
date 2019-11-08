# 现在让用户输入自己的出生年份，再输入出生的日期
# 打印出该用户的属相，输出用户的星座


# sx = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# year = int(input("please input your year: "))
# print(sx[year % 12])

xz = ('水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座',
      '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座')
rq = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22),
      (7, 23), (8, 23), (9, 23), (10, 24), (11, 23), (12, 22))
month = int(input("please input your month: "))
date = int(input("please input your date: "))

for dates in range(len(rq)):
    if (month, date) >= (12, 22) or (month, date) < (1, 20):
        print(xz[-1])
        break
    elif (month, date) >= rq[dates]:
        continue
    else:
        print(xz[dates - 1])
        break

