# number = [12, 23, 34, 42, 56, 64, 73, 82]

# for index in range(len(number)):
#     if number[index] == 64:
#         print("64's index number: {}".format(index))

# 二分查找
search = int(input("please input number: "))
number = [12, 23, 34, 42, 56, 64, 73, 82]
start, stop = 0, len(number) - 1
while stop - start >= 0:
    middle = (start + stop) // 2
    if search > number[middle]:
        start = middle + 1
    elif search < number[middle]:
        stop = middle - 1
    else:
        print("{}'s index number: {}".format(search, middle))
        break
