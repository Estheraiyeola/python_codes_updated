def collect_price_from_user():
    while True:
        try:
            price_of_the_item = int(input('Enter the price of the item: \n'))
            condition = price_of_the_item > 0
            if not condition:
                raise TypeError
        except ValueError:
            print('Invalid input')
        except TypeError:
            print('Positive numbers pls')
        except KeyboardInterrupt:
            print('Interrupted at runtime')
        else:
            return price_of_the_item


def collect_vat_from_user():
    while True:
        try:
            percentage_of_vat = int(input('Enter the percentage of VAT from 1-100: \n'))
            condition = 0 <= percentage_of_vat <= 100
            if not condition:
                raise TypeError
        except ValueError:
            print('Invalid input')
        except TypeError:
            print('Not in the range')
        except KeyboardInterrupt:
            print('Interrupted at runtime')
        else:
            return percentage_of_vat


def your_vat():

    price = collect_price_from_user()
    vat = collect_vat_from_user()

    vat_percentage_value = vat / 100 * price
    vat_plus_price = price + vat_percentage_value
    return vat_plus_price



print(your_vat())
