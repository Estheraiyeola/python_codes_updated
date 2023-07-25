def highest_odd_function(arr):
    new_list = []
    for index in arr:
        if index % 2 == 1:
            new_list.append(index)
    highest = new_list[0]
    for index1 in new_list[1:]:
        if index1 > highest:
            highest = index1
    return highest


arr1 = [19, 2, 3, 4, 9, 55]
print(highest_odd_function(arr1))
