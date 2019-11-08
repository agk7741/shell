# 声明一个字符串的变量
string = 'hello world'

# 字符串的切片，字符串的索引:
# h e l l o   w o r l d
# 0 1 2 3 4 5 6 7 8 9 10
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# print(len(string)) # =? 11
for index in range(len(string)):
    print(string[index])

# 字符串切片, 切片
print(string[1:5])
print(type(string[7:10]))
print(string[:])
print(string[1:])
print(string[:1000000])




