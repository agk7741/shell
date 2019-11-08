
def nn(n):
    def mm(m):
        return m ** n
    return mm


jisuanqi = nn(5)

result = jisuanqi(2)
print(result)

