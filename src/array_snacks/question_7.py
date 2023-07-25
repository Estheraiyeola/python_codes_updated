def check_string_palindrome(str):
    for index in range(len(str)):
        low = 0
        high = index - 1
        while low < high:
            if str[low] < str[high] or str[low] > str[high]:
                print("Not palindrome")
            if str[low] == str[high]:
                low += 1
                high -= 1


str = "abcba"
print(check_string_palindrome(str))
