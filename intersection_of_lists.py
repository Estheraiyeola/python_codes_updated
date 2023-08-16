"""Returns the intersection of lists"""
list1 = [65,20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]


def intersect_of_lists(first_list, second_list):
    global list1, list2
    first_list = set(list1)
    second_list = set(list2)
    intersected_list = []
    for number in first_list:
        if number in second_list:
            intersected_list.append(number)
    return tuple(intersected_list)


print(intersect_of_lists(list1, list2))
