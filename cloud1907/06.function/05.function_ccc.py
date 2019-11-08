def number(n):
    if type(n) not in {str, int}:
        return 'please check your input!!!'
    def opera(m):
        result = 0
        for i in range(m+1):
            # m = 3 = 0+1+2+3
            result += i
        return result
    return opera(n)


print(number(3))
