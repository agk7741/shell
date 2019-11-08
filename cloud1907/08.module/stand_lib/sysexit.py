# 循环结束后会不会还执行后续的动作?
# for i in range(10):
#     if i == 5:
#         break
#     else:
#         print(i)
# print('program continue to...')

import sys

for i in range(10):
    if i == 5:
        sys.exit(12)    # 终止: 程序正常结束; 停止:由程序中某个组件进行的停止操作
    else:
        print(i)
print('program continue to...')
