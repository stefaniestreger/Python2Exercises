"""
Programmer: Stefanie Streger
Assignment: Module 7 - Lab
Date Completed: 10/7/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


class Product:

    def __init__(self):
        self.name = str(input('Name of product: '))
        self.price = float(input('Price of product: '))
        self.discountPercent = int(input('Discount percent amount: '))

    def discount_amount(self):
        discount_total = ((self.discountPercent / 100) * self.price)
        return discount_total

    def discounted_price(self):
        discount_price = self.price - self.discount_amount()
        return discount_price


def main():
    first_product = Product()
    second_product = Product()

    print('PRODUCT DATA')
    print('')
    print('Name: ', first_product.name)
    print('Price: $', first_product.price)
    print('Discount percent: ', format(first_product.discountPercent, '.2f'), '%')
    print('Discount Amount: $', format(first_product.discount_amount(), '.2f'))
    print('Discount Price: $', format(first_product.discounted_price(), '.2f'))
    print('')

    print('PRODUCT DATA')
    print('')
    print('Name: ', second_product.name)
    print('Price: $', second_product.price)
    print('Discount percent: ', format(second_product.discountPercent, '.2f'), '%')
    print('Discount Amount: $', format(second_product.discount_amount(), '.2f'))
    print('Discount Price: $', format(second_product.discounted_price(), '.2f'))


main()
