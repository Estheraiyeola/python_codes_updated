counter = 0
total = 0
required_class = 'SS3'
class_ = input('Enter the class of the students: ')
grade = int(input('Enter the grade except -25: '))
average = 0.0

if class_ == required_class:
    while grade != -25:
        total += grade
        counter += 1

        grade = int(input('Enter another grade or enter -25 to end the program: '))
    if total > 0:
        average_no = total / counter

        print('*' * 70)
        print('\t\tAso Rock Secondary School, Abuja Nigeria')
        print('*' * 70)
        print('Class: ', class_, '\nNumber of Students: ', counter, '\nTotal score: ', total, '\nAverage score: ',
              average_no)
        print('*' * 70)

# else:
#   print('Invalid class!!')
elif class_ != required_class:
    exit()
