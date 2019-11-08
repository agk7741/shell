# 把用户输入的搜索内容进行检测,若有敏感词汇则替换成『*』号显示
# if 's' in 'string':
#     print('s 存在于 string')
# else:
#     print('s 不存在于 string')

# search = input('please input: ')
# word = '苍老师'
# if word in search:
#     search_replace = search.replace('苍老师', '***')
#     print(search_replace)
# else:
#     print(search)


# 验证码输入,比对并验证
import random

check_code = ''
for i in range(2):
    wcode = chr(random.randint(65, 90))
    ncode = random.randint(0, 9)
    n = str(wcode) + str(ncode)
    check_code += n
print("所提示的验证码为: ", check_code)
user_code = input("请输入所提示的验证码: ")
if user_code.lower() == check_code.lower():
    print("登陆成功")
else:
    print("验证码输入错误")



