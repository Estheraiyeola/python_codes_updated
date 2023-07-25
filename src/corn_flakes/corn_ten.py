"""Displaying the First 10 multiples of 5"""

multiples = 1
for number in range(1, 11):
    multiples *= 5
    print(f'{multiples},', end=' ')

# for multiples in range(1, 11): print(f'{5 ** multiples},', end=' ')

