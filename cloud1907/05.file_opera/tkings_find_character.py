# 请统计出tkings.txt中, 『关羽』、『曹操』、『刘备』、『张飞』、『赵云』出现的次数
# 并用字典存储, 形式为: {人物01：次数, 人物02：次数, ...}

file = open(file='./file/tkings.txt', mode='r', encoding='utf8')
content = file.read().replace('\n', '')
character = {}
user = ('关羽', '曹操', '刘备', '张飞', '赵云')
for i in user:
    if i not in character.keys():
        character.setdefault(i, content.count(i))

rank = []
for element in character.items():
    rank.append(element)

for i in range(len(rank)):
    for j in range(len(rank) - 1):
        if rank[j][1] > rank[j+1][1]:
            rank[j], rank[j+1] = rank[j+1], rank[j]
print(dict(rank))

file.close()

# 请统计出tkings.txt中, 『青龙偃月刀』、『丈八蛇矛』、『雌雄双股剑』、『青釭剑』、『方天画戟』
# 出现的次数，用字典存储, 并从大到小排列;
file = open(file='./file/tkings.txt', mode='r')
content = file.read().replace('\n', '').replace(' ', '')
# arms = ('青龙偃月刀', '丈八蛇矛', '雌雄双股剑', '青釭剑', '方天画戟')
# number = {}
# for element in arms:
#     if element not in number.keys():
#         number.setdefault(element, content.count(element))
arms = {'青龙偃月刀': None, '丈八蛇矛': 0, '雌雄双股剑': 0, '青釭剑': 0, '方天画戟': 0}
for keys in arms.keys():
    arms[keys] = content.count(keys)
rank = []
for items in arms.items():
    rank.append(items)
for i in range(len(rank)):
    for j in range(len(rank) - 1):
        if rank[j][1] < rank[j+1][1]:
            rank[j], rank[j+1] = rank[j+1], rank[j]
print(dict(rank))

file.close()








