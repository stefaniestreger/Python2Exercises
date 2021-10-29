"""
Programmer: Stefanie Streger
Assignment: Module 7 - Programming Assignment
Date Completed: 10/7/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import product


def main():
    product_list = []
    keep_going = 'y'

    while keep_going == 'y':
        name = str(input('Enter a product name: '))
        price = float(input('Enter a price for this product: '))
        discount_percent = int(input('Enter a discount percentage: '))
        product_item = product.Product(name, price, discount_percent)
        product_list.append(product_item)
        keep_going = str(input('Enter another product? (Enter y/n): '))
        continue

    print('')
    print('PRODUCTS:')
    print('====================')
    for item in product_list:
        print(item)
        print('')


main()
