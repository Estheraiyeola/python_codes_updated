# def divide_or_square(number):
#     if number % 5 == 0:
#         return number ** 0.5
#     else:
#         return number % 5


def divide_or_square2(number):
    return number ** 0.5 if number % 5 == 0 else number % 5


print(divide_or_square2(100))
