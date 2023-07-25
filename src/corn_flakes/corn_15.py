def asterisks(num):
    for row in range(num):
        for column in range(0, num - row):
            print(" ", end=" ")
        for column in range(row):
            print("*", end=" ")
            print("*", end=" ")
        print()
    for row in range(num):
        for column in range(0, row):
            print(" ", end="")
            print(" ", end="")
        for column in range(num - row, 0, -1):
            print("*", end=" ")
            print("*", end=" ")
        print()


asterisks(5)
