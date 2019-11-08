import random


# print(random.random())
# print(random.uniform(0, 9))
# print(random.randint(1, 9))
# element = (1, 2, 3, 4, 'string', True, False, '1+1')
# print(random.choices(element))
# number = [1, 2, 3, 4, 5]
# random.shuffle(number)
# print(number)


def vcode(number):
    coder = ''
    for i in range(number):
        nums = random.randint(0, 9)
        word = chr(random.randint(65, 90))
        code = random.choices([nums, word])
        coder += str(code[0])
    return coder


print(vcode(5))




