"""Sum of numbers at odd positions"""
numbers = [10, 20, 30, 40, 50]
total = 0
for i in numbers[1:5:2]:
    total = total + i
print(total)