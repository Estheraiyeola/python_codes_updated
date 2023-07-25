def odd_positions(arr):
    new_arr = []
    for index in range(len(arr)):
        if index == 1 or index % 2 == 1:
            new_arr.append(arr[index])
    return new_arr


num = [2, 4, 6, 5, 20, 50, 100, 60, 4, 1, 7, 8, 90]
print(odd_positions(num))
