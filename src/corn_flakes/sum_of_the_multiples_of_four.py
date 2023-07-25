for num in range(1, 11):
    if num % 4 == 0:
        if num == 4:
            total = 1
            sum_ = 0
            for times in range(0, 5):
                total = total * num
                sum_ = sum_ + total
            print(f"{sum_}", end=" ")
        else:
            total = 1
            sum_ = 0
            for times in range(0, 5):
                total = total * num
                sum_ = sum_ + total
            print(f"{sum_}", end=" ")
