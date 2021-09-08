"""
Programmer: Stefanie Streger
Assignment: Module 3 - Lab
Date Completed: 9/8/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


# Main function to handle program
def main():
    new_file = open('mod3numlist.txt', 'r')
    try:
        line1 = new_file.readline()
        even_list = []
        odd_list = []

        while line1 != '':
            x = line1.rstrip('\n').split() # Remove newline and split string

            for item in x:
                valid_num = int(item) # Convert str to int
                if (valid_num % 2) == 0:
                    even_list.append(valid_num) # If item is divisible by 2, append to even list
                else:
                    odd_list.append(valid_num) # Everything else, append to odd list

            line1 = new_file.readline()

        new_file.close()

        create_even(even_list)

        create_odd(odd_list)

    except FileNotFoundError as e:  # Error handling when file isn't found
        print('File name is invalid or does not exist')


# Create file from list of even numbers
def create_even(even_list):
    even_file = open('evennumbers.txt', 'a')
    for num in even_list:
        even_file.write(str(num) + '\n') # Convert int to str, write value with newline added
    even_file.close()


# Create file from list of odd numbers
def create_odd(odd_list):
    odd_file = open('oddnumbers.txt', 'a')
    for num in odd_list:
        odd_file.write(str(num) + '\n') # Convert int to str, write with newline added
    odd_file.close()


main()
