"""Squaring the number at each index and getting the largest and smallest number"""
numbers = [50, 70, 30, 10, 40]
num = []
for i in numbers:
    num.append(i ** 2)

largest = num[0]
smallest = num[0]
for j in num:
    if j > largest:
        largest = j
print(f'The largest number is {largest}')
for k in num:
    if k < smallest:
        smallest = k
print(f'The smallest number is {smallest}')