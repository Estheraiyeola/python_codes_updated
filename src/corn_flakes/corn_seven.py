"""Multiplication Timetable"""


def multiplication_table(num):
    for number in range(1, 13):
        for num in range(1, num + 1):
            product = num * number
            print("%i X %i = %-4i" % (num, number, product), end='\t\t')
        print('\n')
    return 0

multiplication_table(30)