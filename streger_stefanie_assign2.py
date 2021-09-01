"""
Programmer: Stefanie Streger
Assignment: Module 2 - Programming Assignment
Date Completed: 8/31/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""
import conversion


def main():
    title()
    menu()
    menu_choice = str(input('Select a conversion (a/b): '))
    keep_going = 'y'

    while keep_going == 'y':
        if menu_choice != 'a' or menu_choice != 'b':
            print('You must choose a valid menu option. Please make a valid selection.')
            print()
            menu()
            menu_choice = str(input('Select a conversion (a/b): '))
            continue

        if menu_choice == 'a':
            feet = float(input('Enter feet: '))
            print()
            print('The answer is ', conversion.convert_to_meters(feet), 'meters')
            print()
            keep_going = str(input('Would you like to perform another conversion? (y/n): '))
            print()

            if keep_going == 'y':
                menu()
                menu_choice = str(input('Select a conversion (a/b): '))
                continue
            else:
                print('Thanks, bye!')
                break

        if menu_choice == 'b':
            meters = float(input('Enter meters: '))
            print()
            print('The answer is ', conversion.convert_to_feet(meters), 'feet')
            print()
            keep_going = str(input('Would you like to perform another conversion? (y/n): '))
            print()

            if keep_going == 'y':
                menu()
                menu_choice = str(input('Select a conversion (a/b): '))
                continue
            else:
                print('Thanks, bye!')
                break


def title():
    print('Feet and Meters Converter')
    print()


def menu():
    print('Conversions Menu:')
    print('a. Feet to Meters')
    print('b. Meters to Feet')
    print()


main()
