def check_duplicates(arr):
    for index in arr:
        duplicate = index
        index = set(arr)

        if index == duplicate:
            return index






arr1 = ['ade', 'tope', 'alabi', 'daniel', 'daniel']
print(check_duplicates(arr1))
