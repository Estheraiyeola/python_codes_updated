def returns_a_dict(arr):
    new_arr = []
    dictionary = {}
    for index in arr:
        if index[0].lower() == 's':
            new_arr += [index.capitalize()]
    unique_element = set(new_arr)
    key = list(unique_element)
    for index in key:
        counter = 0
        for j in new_arr:
            if index == j:
                counter += 1
                dictionary[index] = counter

    return dictionary


names = ['Joel', 'Daniel', 'seyi', 'Sikiru', 'Muhammad', 'Hakimi', 'Segun', 'Ashley', 'Seyi', 'segun']
print(returns_a_dict(names))
