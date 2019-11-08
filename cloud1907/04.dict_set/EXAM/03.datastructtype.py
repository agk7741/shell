# tuple, list, dict, set
tuple01 = (1, 2, 3, 4, 5)
list01 = [1, 2, 3, 4, 5]
dict01 = dict([('tom', 93), ('tony', 90), ('hale', 34)])
set01 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(tuple01, list01, dict01, set01)

# 遍历: tuple, list
for element in tuple01:
    print(element)
for element in list01:
    print(element)

# list: append, remove
# dict: setdefault, pop
# set: 天然的去重工具

# 求字典的长度
print(len(dict01))

# string
string = 'hello'

