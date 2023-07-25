sumTotal = 0
sum_1 = 0
sum_2 = 0
for num in range(1, 11):
    if num % 4 == 0:
        if num == 4:
            total = 1
            sum_ = 0
            for times in range(0, 5):
                total = total * num
                sum_ = sum_ + total
            sum_1 = sum_
        else:
            total = 1
            sum_ = 0
            for times in range(0, 5):
                total = total * num
                sum_ = sum_ + total
            sum_2 = sum_
sumTotal = sum_1 + sum_2
print(f"{sumTotal}")
