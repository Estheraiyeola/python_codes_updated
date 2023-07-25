def removes_duplicate(arr):
    new_arr = []
    for index in arr:
        if index in new_arr:
            continue
        else:
            new_arr += [index]
    return new_arr


array = [1, 2, 3, 3, 4, 5, 1, 3, 2]
print(removes_duplicate(array))
