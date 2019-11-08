import os

# 列出指定目录下的文件或目录
dir = os.listdir('../05.file_opera')
print(dir)
# 获取当前所在的工作目录的绝对路径
curr_path = os.getcwd()
print(curr_path)
# 改变工作目录
os.chdir('../05.file_opera')
curr_path = os.getcwd()
print(curr_path)
# 判断文件或目录
dir_check = os.path.isdir('file')
print(dir_check)
file_check = os.path.isfile('01.file_io.py')
print(file_check)

# file_name = input("please file's name: ")
# if os.path.isfile(file_name):
#     print('this file is exist.')
# else:
#     print('this file not exist')
# 获取文件的大小或目录的大小
size = os.path.getsize('01.file_io.py')
print(size)
# 获取文件的绝对路径(局限在当前目录中,若想获取其他目录中文件的绝对路径,
# 则需要切换当前目录为要获取绝对路径的目录中)
abspath = os.path.abspath('01.cycle_for.py')
print(abspath)
# 分割文件及目录、文件名与拓展名、连接文件与目录
file_path = '/etc/sysconfig/network-script/ifcfg-ens33'
print(os.path.split(file_path))
file_name = 'hello.py'
print(os.path.splitext(file_name))
fileN = 'world.sh'
dirM = '/etc/cloud1907'
print(os.path.join(dirM, fileN))

path = "/etc/cloud1907/world.sh"
print(os.path.basename(path))
print(os.path.dirname(path))





