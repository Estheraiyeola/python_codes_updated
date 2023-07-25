def running_total(arr):
    total = 0
    for index in range(len(arr)):
        total += arr[index]
        print(total)
    return total


numbers = [1, 2, 3, 4, 5]
print(running_total(numbers))
