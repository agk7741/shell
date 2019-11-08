# 集合的声明
set01 = {1, 3, 2, 4}
print(set01)

list01 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
set02 = {1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4}
print(list01)
print(set02)

# 交集和并集
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# setA和setB共有的元素是？
setC = setA & setB
print(setC)

# setA和setB的并集
setD = setA | setB
print(setD)

if 5 in setD:
    print(True)
else:
    print(False)

# setE = {1, 2, 3, {4, 5}, 6, 7, 8}
# if setC in setE:
#     print(True)
# else:
#     print(False)


setF = {1, 2, 3, 4, 5}
setF.add('hello')
print(setF)

setF.update([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(setF)

setF.remove(1)
print(setF)

list01 = list(setF)
print(list01, type(list01))


