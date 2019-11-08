# 声明一个字典
dict01 = {}

# 增加字典中的键值对儿
dict01['tony'] = 100
print(dict01)

dict01.setdefault('natasha', 95)
print(dict01)

dict01.update([('tom', 89), ('a', 90), ('b', 90), ('c', 90)])
print(dict01)

list01 = ['tom', 'tony', 'hale']
dict02 = {}.fromkeys(list01)
print(dict02)

# 删除
dict02.pop('tom')
print(dict02)

dict02.popitem()
dict02.popitem()
print(dict02)

# 更改
