counter = 0
total = 0
required_class = 'SS3'
class_ = input('Enter the class of the student: ')

if class_ == required_class:
    while counter < 20:
        grade = int(input('Enter the grade of the student: '))
        total += grade
        counter += 1

    average_no = float(total) / counter

    print('*' * 70)
    print('\t\tAso Rock Secondary School, Abuja Nigeria')
    print('*' * 70)
    print('Class: ', class_, '\nNumber of Students: ', counter, '\nTotal score: ', total, '\nAverage score: ',
          average_no)
    print('*' * 70)