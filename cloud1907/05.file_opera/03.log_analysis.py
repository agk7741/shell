
# 1.文件的位置：access_log是存于一个目录下的, 或者与分析程序保持在同一个目录
# 2.所用到的知识点：str、dict
# 3.观察好access_log日志的分布情况,第一列都是IP地址，第七列都是访问资源，第九列都是状态码
with open(file='./file/access_log', mode='r') as file:
    ips = {}    # 声明一个空的字典,用来接收文件中的IP地址及次数
    for lines in file.readlines():
        op = lines.split()
        if op[0] not in ips.keys():
            ips.setdefault(op[0], 1)
        else:
            ips[lines.split()[0]] += 1
    ip = []
    for items in ips.items():
        ip.append(items)
    for i in range(len(ip)):
        for j in range(len(ip) - 1):
            if ip[j][1] < ip[j+1][1]:
                ip[j], ip[j+1] = ip[j+1], ip[j]
    print(dict(ip[:2]))



