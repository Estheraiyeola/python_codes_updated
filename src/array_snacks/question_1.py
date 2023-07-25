def largest(arr):
    max_ = arr[0]
    for index in arr[1:]:
        if index > max_:
            max_ = index
    return max_


num = [52, 1, 5, 2]
print(largest(num))
