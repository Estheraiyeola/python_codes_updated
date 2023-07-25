"""Palindromes in string"""


# def is_palindrome(string):
#     return string == string[::-1]


def is_palindrome2(string):
    string = lambda str2: string == string[::-1]
    return string


print(is_palindrome2("moyin"))
