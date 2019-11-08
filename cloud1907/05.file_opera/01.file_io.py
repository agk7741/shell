# open()函数可以打开文件, 并且规定文件的读写模式, 并规定好读取文件时或写入内容时的字符编码
file = open(file='./file/file.txt', mode='r', encoding='utf8')

# 读取整个文件的内容
content = file.read()
print(content)

# 逐行读取文件的内容
content = file.readline()
text = file.readline()
print(content)
print(text)

# 读取文件的每一行, 并把每一行放入到列表中
content = file.readlines()
print(content)

# 关闭打开的文件
file.close()

text = open(file='./file/file.txt', mode='a', encoding='utf8')

text.write('\nthis is four line.')

text.close()
