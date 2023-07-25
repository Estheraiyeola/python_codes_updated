"""Down_payment for an item based on their credit score"""

user = int(input('Enter the price: '))
users_credit_score = input('Do you have a good credit Score: True / False ')

if users_credit_score:
    if users_credit_score == 'True' or users_credit_score == 'true':
        ten_percentage_discount = user * 0.1
        new_amount = user - ten_percentage_discount
        print(f'A 10% discount has been applied to your item, your new price is {new_amount}')
        ten_percentage_down_payment = new_amount * 0.1
        down_payment = new_amount - ten_percentage_down_payment
        print(f'The initial amount to be payed is {ten_percentage_down_payment}')
    elif users_credit_score == 'False' or users_credit_score == 'false':
        twenty_five_percentage = user * 0.25
        amount = user - twenty_five_percentage
        print('You have a bad credit score!!')
        print(f'The initial amount to be payed is {twenty_five_percentage}')
    else:
        print('Get a good credit score')