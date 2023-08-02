"""Determines the number of males or females in a class which have been saved in a list"""


def counter(arr):
    male_counter = 0
    female_counter = 0
    arr = arr
    for i in arr:
        if 'Male' == i or 'male' == i:
            male_counter += 1
        elif 'Female' == i or 'female' == i:
            female_counter += 1
    new_list = [('Male', male_counter), ('Female', female_counter)]
    return new_list


array = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male',
         'female']
print(counter(array))
