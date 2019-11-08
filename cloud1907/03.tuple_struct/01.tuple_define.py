# python中四种数据结构类型: 元组、列表、字典、集合
# 元组的定义: 元组在Python具有不可变性
t01 = (1, 2, 3, 4, 5)
t02 = (1, 'hello', True, 3.14)
t03 = (1,)

# 元组的索引确定，遍历元组中每一个元素
t01_len = len(t01)
for index in range(t01_len):
    print(t01[index])

# 找出元组中的偶数
for index in range(t01_len):
    if t01[index] % 2 == 0:
        print(t01[index])

# 切片输出
print(t01[1:2+1])
print(t01[-3:-2+1])
print(t01[-3:4])


