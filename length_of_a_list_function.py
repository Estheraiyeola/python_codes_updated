def length_of_a_list(collection):
    counter = 0
    for index in collection:
        counter += 1
    return counter


collections = [1, 2, 3, 4, 6]
print(length_of_a_list(collections))
