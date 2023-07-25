def greater(num_1, num_2, num_3, num_4):
    maximum = num_1
    print(maximum)
    if num_2 > num_1:
        maximum = num_2
        print(maximum)
    if num_3 > num_1:
        maximum = num_3
        print(maximum)
    if num_4 > num_1:
        maximum = num_4
        print(maximum)
    print(maximum)



greater(1, 3, 2, 4)


def lowest(num1, num2, num3, num4):
    minimum = num1
    if num2 < num1:
        minimum = num4
    if num3 < num1:
        minimum = num4
    if num4 < num1:
        minimum = num4
    print(minimum)


lowest(4, 2, 3, 1)
