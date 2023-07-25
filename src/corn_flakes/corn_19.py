"""Sum of numbers at even positions"""
numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers[0:5:2]:
    total = total + i
print(total)
