import random


def main():
    title()

    selection = str(input('Roll the dice? (y/n): '))

    keep_going = 'y'
    while keep_going == 'y':
        roll_dice()
        keep_going = str(input('Roll the dice? (y/n): '))
        if keep_going == 'y':
            continue
        else:
            print('Bye!')
            print()
            break


def title():
    print('Dice Roller')


def roll():
    roll_value = random.randint(1, 6)
    return roll_value


def roll_dice():
    first = roll()
    second = roll()
    print('Die 1: ', first)
    print('Die 2: ', second)

    total_dice = (first + second)
    print('Total: ', total_dice)
    print()

    if first == 1 and second == 1:
        print('Snake eyes!')

    if first == 2 and second == 2:
        print('Ballerina!')

    if first == 4 and second == 4:
        print('Square Pair!')

    if first == 6 and second == 6:
        print('Boxcars!')


main()
