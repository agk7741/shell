def logAnalysis(path, index=0):
    with open(file=path, mode='r') as file:
        continer = {}
        for lines in file.readlines():
            if lines.split()[index] not in continer.keys():
                continer.setdefault(lines.split()[index], 1)
            else:
                continer[lines.split()[index]] += 1
    return continer


def mp(d):
    ips = []
    for items in d.items():
        ips.append(items)
    for i in range(len(ips)):
        for j in range(len(ips) - 1):
            if ips[j][1] < ips[j+1][1]:
                ips[j], ips[j+1] = ips[j+1], ips[j]
    return dict(ips)


status_code = logAnalysis(path='access_log', index=8)
http_code = ('404', '200')
for keys in status_code.keys():
    if keys in http_code:
        print(keys, status_code[keys])

ips = logAnalysis(path='access_log')
result = mp(ips)
print(result)


a = mp
result = a(ips)
print(result)



