# import re
#
#
# data = 'Last login: Thu Mar  2 10:04:52 2019 from 39.100.110.135'
# print(data.split())
# regular_text = re.split(pattern='[:.] *', string=data)
# print(regular_text)
#
# data01 = 'What is the difference between python 2.7.13 and python 3.7.3 ?'
# data02 = 'What is the difference between python 2.8.17 and python 3.8.3 ?'
# # regular_text01 = re.findall(pattern='python [0-9].[0-9].[0-9]{1,2}', string=data01)
# # regular_text02 = re.findall(pattern='python [0-9].[0-9].[0-9]{1,2}', string=data02)
# # print(regular_text01)
# # print(regular_text02)
#
# regular = re.compile(pattern='python [0-9].[0-9].[0-9]{1,2}')
# text01 = regular.findall(data01)
# text02 = regular.findall(data02)
# print(text01)
# print(text02)

import re


def getIp(filepath):
    with open(file=filepath, mode='r') as log:
        ips = {}
        for lines in log.readlines():
            regular = re.compile(pattern='[1-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[1-9]{1,3}')
            ip = regular.findall(lines)
            if ip[0] not in ips.keys():
                ips.setdefault(ip[0], 1)
            else:
                ips[ip[0]] += 1
        ips = dict(sorted(ips.items(), key=lambda x: x[1], reverse=True))
        return ips


ip_dict = getIp('access_log')
print(ip_dict)








