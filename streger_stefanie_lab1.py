"""
Programmer: Stefanie Streger
Assignment: Module 1 - Lab
Date Completed: 8/24/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


def main():
    start_num = int(input('Enter a Starting number: '))
    stop_num = int(input('Enter a Stop number: '))
    print('                  ')

    while start_num >= stop_num:
        print('Please enter a Starting number less than Stop number')
        print('                  ')
        start_num = int(input('Enter a Starting number: '))
        stop_num = int(input('Enter a Stop number: '))
        break

    print("Number\t\tSquared\t\tCubed")
    print("======\t\t=======\t\t=====")
    print(create_table(start_num, stop_num))


def create_table(start, stop):
    for item in range(start, stop + 1):
        square = item ** 2
        cube = item ** 3
        print(item, '\t\t', square, '\t\t', cube)


main()
