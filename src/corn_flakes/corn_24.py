def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


def sum_(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


def max_(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_(list[1:])
    return list[0] if list[0] > sub_max else sub_max


list = [1, 2, 5, 4, 70, 65]
print(sum_(list))
print(list[0:])
print(max_(list))
