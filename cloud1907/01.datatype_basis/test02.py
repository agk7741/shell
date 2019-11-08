
# rmb = 1000
# rate = 7.1168
# usd = rmb / rate
# print(usd)

# rmb = int(input('please input: '))
# rate = 7.1168
# print(rmb/rate)

# age = int(input('please your age: '))
# if age > 0 and age <= 18:
#     print('未成年')
# elif age >= 19 and age <= 35:
#     print('正当年')
# elif age > 35 and age <= 65:
#     print('老年')
# else:
#     print('棺材年')


number = int(input('please input: '))
if number % 3 == 0 and number % 9 == 0:
    print(number)
else:
    print(False)

