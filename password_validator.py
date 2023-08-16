import re
import string


def password_validator():
    password = input('Enter a password:\n')
    special_characters = set(string.punctuation)
    if len(password) < 8:
        print("Not long enough")
        password_validator()
    if not re.search(r'[a-z]', password):
        print('No Small Letter')
        password_validator()
    if not re.search(r'[A-Z]', password):
        print('No Capital Letter')
        password_validator()
    if not re.search(r'[0-9]', password):
        print('No digits')
        password_validator()
    if not any(char in special_characters for char in password):
        print('No special characters')
        password_validator()
    else:
        print('Correct Password')



print(password_validator())
