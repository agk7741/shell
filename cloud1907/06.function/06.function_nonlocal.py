def waibu():
    x = 90
    def neibu():
        nonlocal x
        x = 33
        print(x)
    neibu()
    print(x)


waibu()
