def checks_for_elements(arr, item):
    pivot = arr[0]
    index = 1
    while pivot != item and index != len(arr):
        pivot = arr[index]
        index += 1
    if pivot != item:
        print(f'''
Input not found''')
    else:
        print(f'''
    The element {pivot} was found at index {index}''')
    return pivot


num = [2, 4, 6, 5, 20, 50, 100, 60, 4, 1, 7, 8, 90]
print(checks_for_elements(num, 90))
