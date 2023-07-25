for numbers in range(1, 11):
    if numbers % 2 == 1 and numbers != 9:
        print(f"{numbers},", end=" ")
    if numbers == 9:
        print(f"{numbers}", end="")