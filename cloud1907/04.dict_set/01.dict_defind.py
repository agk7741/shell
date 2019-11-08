# 字典的声明方式
#           key(键: 唯一性) :  value(值: 无局限性)
dict01 = {'name': 'bavdu', 'age': 18, 'sex': 'man'}
dict02 = {'tom': 94, 'hale': 99, 'jerry': 90}

dict03 = dict({'name': 'bavdu', 'age': 18, 'sex': 'man'})
print(dict03, type(dict03))

dict04 = dict([('name', 'bavdu'), ('age', 18), ('sex', 'man')])
print(dict04, type(dict04))

dict05 = dict(name='bavdu', age=18, sex='man')
print(dict05, type(dict05))

# 变量 = (int,float,str,bool)(tuple,list,dict,set)

# 对于字典如何使用for进行遍历
# 元组和列表他们索引都是数字, 但是字典中的索引却是键
# [1, 2, 3, 4, 5] == {0:1, 1:2, 2:3, 3:4, 4:5}
for keys in dict05.keys():
    print(keys)
for values in dict05.values():
    print(values)
for items in dict05.items():
    print(items)

# 字典的嵌套(既可以嵌套字典,也可以嵌套列表和元组)
mins1 = getCpu(1)
mins2 = getCpu(5)
mins3 = getCpu(15)
info = {
    'software_info': {
        'cpu_rate': [mins1, mins2, mins3],
        'process': getProcess()
    },
    'hardware_info': {
        'cpu_version': ('Inter Core E...'),
        'memory_version': (),
        'disk_version': ()
    }
}




