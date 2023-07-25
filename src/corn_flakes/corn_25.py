numbers = [2, 8, 9, 5, 6, 2]


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        sub_arr_small = [i for i in arr[1:] if i <= pivot]
        sub_arr_big = [i for i in arr[1:] if i > pivot]
        return quicksort(sub_arr_small) + pivot + quicksort(sub_arr_big)

print(numbers)
print(quicksort(numbers))
