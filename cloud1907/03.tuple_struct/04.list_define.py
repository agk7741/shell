# 列表的定义
number = [1, 2, 3, 4, 5]

# 切片: 支持索引
print(number[2:3+1])
# 遍历: for遍历
for index in range(len(number)):
    print(number[index])
# 关于列表中的方法: 增、删、改、查
# 列表中增加元素的方法
number.append(6)
print("append", number)

number.insert(2, 7)
print("insert", number)

string = ['hello', 'world', 'python', 'go']
number.extend(string)
print(number)

# 列表中删除元素的方法
number.pop(2)
print(number)

number.remove('go')
print(number)

# number.clear()
# print(number)
#
# del number
# print(number)

# 列表中更改元素的方法
number[-1] = 'PYTHON'
print(number)

# 列表中查找元素的方式
index = number.index('hello', 4, 7)
print(index)

count = number.count(6)
print(count)

number01 = number.copy()
print(number01)

number.reverse()
print(number)

number02 = [23, 45, 67, 12, 34, 56]
number02.sort()
print(number02)




