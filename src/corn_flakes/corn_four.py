"""Password Checker"""
password = input('Enter the password: ')

while len(password) < 8:
    password = input('Enter the password again: ')
print(f'Your password is secure, the length is {len(password)}')
