def calculate():
    val_list = []
    for val in range(3):
        val = input("")
        val_list.append(val)

    val1 = int(val_list[0])
    operators = val_list[1]
    val2 = int(val_list[2])
    total = 0
    if operators == "+":
        total = val1 + val2
        return total
    elif operators == "-":
        total = val1 - val2
        return total
    elif operators == "*":
        total = val1 * val2
        return total
    elif operators == "/":
        total = val1 / val2
        return total
    else:
        return "Logic Error"

