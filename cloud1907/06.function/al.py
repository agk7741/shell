def logAnalysis(abspath, mode):
    def ips():
        with open(file=abspath, mode='r') as log:
            ips = {}
            for lines in log.readlines():
                if lines.split()[0] not in ips.keys():
                    ips.setdefault(lines.split()[0], 1)
                else:
                    ips[lines.split()[0]] += 1
        return ips
    def code():
        pass
    def source():
        pass
    if mode == 'ip':
        return ips
    elif mode == 'code':
        return code
    elif mode == 'source':
        return source
    else:
        return 'not found this function.'


ipAnalysis = logAnalysis('access_log', 'ip')
ipAddress = ipAnalysis()
print(ipAddress)
