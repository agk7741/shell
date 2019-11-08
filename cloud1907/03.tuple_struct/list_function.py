number = [1, 2, 3]
# 增: append, insert, extend
number.append(4)
print("number append: {}".format(number))

number.insert(0, 5)
print("number insert: {}".format(number))

n = [6, 7, 8]
number.extend(n)
print("number extend: {}".format(number))

# 删: pop, remove, clear, del
number.pop(0)
print("number pop: {}".format(number))

number.remove(7)
print("number remove: {}".format(number))

# number.clear()
# print("number clear: {}".format(number))
#
# del number
# print(number)

# 改:
number[0] = '111'
print(number)

# 查: index, count
a = number.index('111')
print(a)

b = number.count(2)
print(b)

op = number.copy()
print(op)

number.reverse()
print(number)

c = [23, 12, 45, 34, 67, 56]
c.sort()
print(c)
