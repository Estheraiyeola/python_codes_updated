for numbers in range(1,11):
    if numbers % 4 == 0 and numbers != 8:
        print(f"{numbers},", end=" ")
    if numbers == 8:
        print(f"{numbers}", end="")