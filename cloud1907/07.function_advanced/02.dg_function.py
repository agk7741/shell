# 递归的声明
# 计算1~10的阶乘 == 1 * 2 * 3 * ... * 10 == 3628800
result = 1
for n in range(1, 11):
    result *= n
print(result)


def dog(n):
    if n == 1:
        return n
    return n * dog(n-1)
# 第一次执行: dog(10) -->> return: 10 * dog(10-1)
#                                      -->> 10 * dog(9) -->>  10 * 9 * dog(9-1)
# 最后一次执行: dog(1) -->> return: 1* dog(1-1)
print(dog(10))

import os

dirC = fileC = 0
def getDir(path):
    for file in os.listdir(path):
        fileAbs = os.path.join(path, file)
        if os.path.isdir(fileAbs):
            global dirC
            dirC += 1
            getDir(fileAbs)
        else:
            global fileC
            fileC += 1
    return dirC, fileC


dir_count, file_count = getDir('/Users/liuchao/Documents/github/cloud1907/05.file_opera')
print('''dir count: {}
file count: {}
'''.format(dir_count, file_count))
print(os.listdir('/Users/liuchao/Documents/github/cloud1907/05.file_opera'))