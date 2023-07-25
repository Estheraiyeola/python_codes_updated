"""Displaying the multiples of 2 lesser than 2000"""
multiples = 2
counter = 0
while multiples < 2000:
    multiples *= 2
    counter += 1
print('The multiples of 2 lesser than 2000 =', multiples)
print('It was multiplied', counter, 'times')
