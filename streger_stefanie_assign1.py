"""
Programmer: Stefanie Streger
Assignment: Module 1 - Lab
Date Completed: 8/24/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


def main():
    print('Shipping Calculator')
    print('=================================================')
    item_cost = float(input('Enter cost of items ordered: '))
    print('')

    keep_going = 'y'

    while keep_going == 'y':
        if item_cost <= 0:
            print('You must enter a positive number. Please try again.')
            print('')
            item_cost = (float(input('Enter cost of items ordered: ')))
            print('')
            continue

        if item_cost > 0:
            show_total_cost(item_cost)
            keep_going = str(input('Continue? (y/n): '))
            print('')
            if keep_going == 'y':
                print('=================================================')
                item_cost = float(input('Enter cost of items ordered: '))
                continue
            else:
                print('=================================================')
                print('Bye!')
                break


def shipping_calculator(item_cost):
    shipping = 5.95
    new_shipping = 0
    if item_cost < 30:
        new_shipping = shipping
    if item_cost >= 30:
        new_shipping = shipping + 2
    if item_cost >= 50:
        new_shipping = shipping + 4
    if item_cost >= 75:
        new_shipping = 0
    return new_shipping


def show_total_cost(item_cost):
    if item_cost < 75:
        total_cost = item_cost + shipping_calculator(item_cost)
        print('Shipping cost:', format(shipping_calculator(item_cost), ',.2f'))
        print('Total cost:', format(total_cost, ',.2f'))
    else:
        free_cost = item_cost
        print('Shipping cost:', 'FREE')
        print('Total cost:', format(free_cost, ',.2f'))
    return


main()
