# 元组,列表,字典,集合
stuple = (1, 2, 3.14, 'string', True)
print(stuple.index(1))
print(stuple.count(1))

for element in stuple:
    print(element)

for index in range(len(stuple)):
    print(stuple[index])

# 元组的切片
print(stuple[1:4])
# 元组解包
element = stuple[1:4]
var01, var02, var03 = element
print(var01, var02, var03)

# 列表
slist = [1, 2, 3.14, 'string', False]
print(slist.index(1))
print(slist.count(0))

# 列表中增加元素
slist.append(True)
print(slist)

slist.extend([1, 2, 3, 4, 5, 6])
print(slist)

slist.insert(2, 4.445)
print(slist)

# 列表中删除元素
slist.pop(2)
print(slist)

slist.remove(True)
slist.remove(True)
slist.remove(True)
print(slist)

# del slist

# 更改列表中的元素
slist[0] = 'two'
print(slist)

slist.reverse()
print(slist)

# 列表中的查询
# for element in slist:
#     print(element)

for index in range(len(slist)):
    if type(slist[index]) in (int, float):
        print(slist[index])


# 列表的排序
number = [23, 12, 34, 24, 56, 64]
number.sort(reverse=True)
print(number)

number01 = number.copy()
print(number01)

number02 = number
print(number02)

# 字典
dict01 = {"key01": 12, "key02": 13, "key03": 14}
dict02 = dict([("key01", 12), ("key02", 13), ("key04", 14)])
print(dict01)
print(dict02)

# 字典的增加操作
dict01['key05'] = 15
print(dict01)

dict01.setdefault('key06', 16)
print(dict01)

dict01.update([('key07', 17), ('key08', 18)])
print(dict01)

# fromkeys
slist = [('key01', 1), ('item01', 2), ('iterable01', 3)]
print({}.fromkeys(slist))

# 字典中的删除
dict01.pop('key01')
print(dict01)

dict01.popitem()
print(dict01)

# 字典中的更改
dict01.update([('key07', 7777)])
print(dict01)

dict01['key07'] = 7777777
print(dict01)

# 字典中的查找
for keys in dict01.keys():
    print(keys)
for values in dict01.values():
    print(values)
for items in dict01.items():
    print(items)

# 字典排序
ips = {'1.1.1.1': 34, '2.2.2.2': 12, '3.3.3.3': 899, '4.4.4.4': 11}
ips_sort = sorted(ips.items(), key=lambda x: x[1], reverse=True)
print(dict(ips_sort))
# ips_list = []
# for items in ips.items():
#     ips_list.append(items)
# print(ips_list)
# for i in range(len(ips_list)):
#     for j in range(len(ips_list) - 1):
#         if ips_list[j][1] < ips_list[j+1][1]:
#             ips_list[j], ips_list[j+1] = ips_list[j+1], ips_list[j]
# print(dict(ips_list))
