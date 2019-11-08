with open(file='./file/access_log', mode='r') as file:
    http_code, status_code = {}, ('400', '401', '402', '403', '404', '405', '406', '407', '408', '409')
    for lines in file.readlines():
        if lines.split()[8] not in http_code.keys() and lines.split()[8] in status_code:
            http_code.setdefault(lines.split()[8], 1)
        elif lines.split()[8] in http_code.keys():
            http_code[lines.split()[8]] += 1
    http_codes = []
    for items in http_code.items():
        http_codes.append(items)
    for i in range(len(http_codes)):
        for j in range(len(http_codes) - 1):
            if http_codes[j][1] < http_codes[j+1][1]:
                http_codes[j], http_codes[j+1] = http_codes[j+1], http_codes[j]
    print(dict(http_codes))
