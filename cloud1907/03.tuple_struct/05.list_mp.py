number = [23, 45, 67, 12, 34, 56]

for i in range(len(number)):
    for j in range(len(number) - 1):
        if number[j] > number[j + 1]:
            number[j], number[j+1] = number[j+1], number[j]
print(number)

# i = 0
# j = 0
# number[0] > number[0 + 1] ==>> False!
# j = 1
# number[1] > number[1 + 1] ==>> False!
# j = 2
# number[2] > number[2 + 1] ==>> True! ==>> [23, 45, 12, 67, 34, 56]
# j = 3
# number[3] > number[3 + 1] ==>> True! ==>> [23, 45, 12, 34, 67, 56]
# j = 4
# number[4] > number[4 + 1] ==>> True! ==>> [23, 45, 12, 34, 56, 67]





