# string exam
string = 'hello world'

# 切片: 索引的确定
string_len = len(string)
string_index_max = string_len - 1

for index in range(string_len):
    print(string[index])

print(string[2:5])
print(string[:])

# 字符串中的一些方法
string_new = string.split()
print(string_new)

string_replace = string.replace('o', '0')
print(string_replace)

# 格式化输出
name = 'op'
ages = 18
sexs = 'man'
print("i am name, age is ages, my sex sexs")
# print("i am " + name + ", " + "age is " + str(ages) + ", ")
print("i am {}, age is {}, my sex {}".format(name, ages, sexs))
