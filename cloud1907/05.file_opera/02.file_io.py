# 文件的自动关闭功能
# file = open(file='./file/file.txt', mode='r')
# file.close()

with open(file='./file/file.txt', mode='a') as file:
    file.write('\nthis is five line.')

with open(file='./file/tkings.txt', mode='r') as file:
    content = file.read().replace('\n', '').replace(' ', '')
    arms = {'青龙偃月刀': 0, '丈八蛇矛': 0, '雌雄双股剑': 0, '青釭剑': 0, '方天画戟': 0}
    for keys in arms.keys():
        arms[keys] = content.count(keys)


