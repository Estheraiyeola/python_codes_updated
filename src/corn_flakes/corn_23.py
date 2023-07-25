numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]


def sorted_list(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
    print(list)


def sorted_list2(list):
    num = []
    for i in list[9:0:-1]:
        num.append(i)
    print(num)


sorted_list2(numbers)
