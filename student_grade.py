import time
import sys

no_of_students = 0
no_of_subjects = 0
storage = []
average_storage = []


def collect_no_of_students_and_subjects():
    global no_of_students, no_of_subjects
    try:
        no_of_students = int(input('How many students do you have?\n'))
        no_of_subjects = int(input('How many subjects do they offer?\n'))
        condition = no_of_students > 0 and no_of_subjects > 0
        if not condition:
            raise TypeError
    except TypeError:
        print('Invalid number')
    except ValueError:
        print('Invalid input')


def create_storage_for_students_subject():
    global no_of_students, no_of_subjects, storage
    storage = [[0 for column in range(no_of_subjects + 2)] for row in range(no_of_students)]
    return storage


def saving_method():
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")
    print('Saved successfully')


def student_grade_interface():
    global storage, no_of_students, no_of_subjects
    rows = no_of_students
    columns = no_of_subjects
    create_storage_for_students_subject()
    for index in range(rows):
        for idx in range(columns):
            print(f'Entering score for student {index + 1}')
            score = int(input(f'Enter score for subject {idx + 1}\n'))
            storage[index][idx] = score
            saving_method()
    return storage


def total_for_each_student():
    global no_of_students, no_of_subjects, storage
    total = 0
    for index in range(no_of_students):
        for idx in range(no_of_subjects):
            total += storage[index][idx]
        storage[index][no_of_subjects] = total
        total = 0
    return storage


def total_for_each_subject():
    global no_of_students, no_of_subjects, storage
    total_for_subject_storage = []
    total = 0
    for index in range(no_of_subjects):
        for idx in range(no_of_students):
            total += storage[idx][index]
        total_for_subject_storage.append(total)
        total = 0
    storage.append(total_for_subject_storage)
    return storage


def average_for_each_student():
    global no_of_students, no_of_subjects, storage
    average_storage_for_each_student = []
    average = 0
    for index in range(no_of_students):
        for idx in range(no_of_subjects):
            average = storage[index][no_of_subjects] / no_of_subjects
        average_storage_for_each_student.append(average)
        average = 0
    average_storage.append(average_storage_for_each_student)
    return average_storage


def average_for_each_subject():
    global no_of_students, no_of_subjects, storage
    average_storage_for_each_subject = []
    average = 0
    for index in range(no_of_subjects):
        for idx in range(no_of_students):
            average = storage[no_of_students][index] / no_of_students
        average_storage_for_each_subject.append(average)
        average = 0
    average_storage.append(average_storage_for_each_subject)
    return average_storage

def display_table():
    global  no_of_students, no_of_subjects, storage
    print('STUDENT\t\t')
    for index in range(no_of_subjects):
        print(f'SUB{index}')
    print('TOT\t\t')
    print('AVE\t\t')
    print('POS\t')
collect_no_of_students_and_subjects()
create_storage_for_students_subject()
saving_method()
student_grade_interface()
total_for_each_student()
total_for_each_subject()
average_for_each_student()
average_for_each_subject()
display_table()
