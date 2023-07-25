def sum_for_loop(arr):
    total = 0
    for index in range(len(arr)):
        total += arr[index]
    return total


def sum_while_loop(arr):
    total = 0
    index = 0
    while index < len(arr):
        total += arr[index]
        index += 1
    return total
def sum_do_while_loop(arr):
    total = 0
    index = 0
    condition = index < len(arr)
    while condition:
        total += arr[index]
        if index == len(arr) - 1:
            return total
        index += 1
number = [1, 2, 3, 4, 5]
print(sum_for_loop(number))
print(sum_while_loop(number))
print(sum_do_while_loop(number))

