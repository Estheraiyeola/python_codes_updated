for numbers in range(1, 11):
    if numbers % 2 == 0 and numbers != 10:
        print(f"{numbers},", end=" ")
    if numbers == 10:
        print(f"{numbers}", end="")