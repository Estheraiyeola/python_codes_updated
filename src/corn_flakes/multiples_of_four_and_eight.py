for num in range(1, 11):
    if num % 4 == 0:
        total = 1
        for times in range(0, 5):
            total = total * num
            print(f"{total}", end=" ")
