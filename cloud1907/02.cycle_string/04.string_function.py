# 声明一个字符串
string = 'Hello World Kitty Tom'

# 分割操作;
string_split = string.split("o")
print(string_split)
# 替换操作;
string_replace = string.replace('Tom', 'TOM')
print(string_replace)
# 大小写转换
string_upper = string.upper()
print(string_upper)
string_lower = string.lower()
print(string_lower)
# 删除首尾的空格
string = 'oaoop_era_oooo'
string_strip = string.strip('o')
# op_era_o
# p_era_
print(string_strip)

string_lstrip = string.lstrip('o')
print(string_lstrip)
string_rstrip = string.rstrip('o')
print(string_rstrip)




