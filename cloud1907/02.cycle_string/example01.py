# 把句子『this is my house』进行反转, 反转的结果为: house my is this
a = 'this is my house'
a_new = a.split()
print(a_new)

a_new_len = len(a_new) - 1
jz = ''
while a_new_len >= 0:
    el = a_new[a_new_len] + ' '
    jz += el
    a_new_len -= 1
print(jz)
