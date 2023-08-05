card_number = ''
int_array = []
is_valid = True
output = ''


def collect_card_number() -> str:
    global card_number
    card_number = input('Hello, Kindly enter card details to verify\n')
    return card_number


def get_length_of_card_number() -> int:
    global card_number
    length = len(card_number)
    return length


def get_the_type_of_card() -> str:
    global card_number
    if card_number.startswith('4'):
        card_type = 'Visa Card'
    elif card_number.startswith('5'):
        card_type = 'MasterCard'
    elif card_number.startswith('37'):
        card_type = 'American Express Card'
    elif card_number.startswith('6'):
        card_type = 'Discover Cards'
    else:
        print('Invalid card type')
        exit(0)
    return card_type


def converts_string_into_an_array() -> list:
    global int_array, card_number
    for index in card_number:
        int_array += [index]
    int_array = list(map(int, int_array))
    return int_array


def get_even_counter(even_counter, index):
    global int_array
    if index % 2 == 0:
        number = int_array[index] * 2
        if number > 9:
            first_number = number / 10
            second_number = number % 10
            number = first_number + second_number
        even_counter += number
    return even_counter


def get_odd_counter(odd_counter, index):
    global int_array
    if index % 2 == 1:
        odd_counter += int_array[index]
    return odd_counter


def validator_algorithm():
    global is_valid
    even_counter = 0
    odd_counter = 0
    for index in int_array:
        even_counter = get_even_counter(even_counter, index)
        odd_counter = get_odd_counter(odd_counter, index)
    add = even_counter + odd_counter
    if add % 10 == 0:
        is_valid = True
    if add % 10 != 0:
        is_valid = False
    return is_valid


def validity_status() -> str:
    global output, is_valid
    if is_valid:
        output = 'Valid'
    if not is_valid:
        output = 'Invalid'
    return output


def display_information():
    print(f'''
    **Credit Card Type: {get_the_type_of_card()}
    **Credit Card Number: {card_number}
    **Credit Card Digit Length: {get_length_of_card_number()}
    **Credit Card Validity Status: {validity_status()}
    ''')


def verifies_information_of_card():
    print(collect_card_number())
    get_the_type_of_card()
    print(converts_string_into_an_array())
    validator_algorithm()
    display_information()


verifies_information_of_card()
