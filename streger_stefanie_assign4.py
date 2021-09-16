"""
Programmer: Stefanie Streger
Assignment: Module 4 - Programming Assignment
Date Completed: 9/15/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


def main():
    read_file = read_data()  # Store list variable
    while True:
        display_menu() # Display menu to user
        menu_choice = int(input('Enter your food group choice: (1-5) ')) # Ask user to input a menu value
        if menu_choice == 1: # Begin if/else loop for menu choices
            dairy_list = create_separate_list(read_file, menu_choice) # Store results of create_separate_list function in list variable
            dairy_list.sort() # Sort the list variable
            print('Name\t\t\tAmount\t\t\tCalories') # Header for columns
            print('---------------------------------------')
            for list_item in dairy_list: # Iterate over list variable to extract individual list items
                name = list_item[0]
                serving = list_item[1]
                calories = list_item[2]
                print(name, '\t\t\t', serving, '\t\t\t', calories) # Print list items with formatting
            print('')
            more_food = input('Would you like to perform another conversion? (y/n): ') # Ask user to continue
            print('')
            if more_food == 'y': # Continue with While loop if user chooses yes
                continue
            else: # End program if user chooses no
                print('Thanks, bye!')
                break
        if menu_choice == 2: # This continues same loop as first 'if' for all menu choices
            meat_list = create_separate_list(read_file, menu_choice)
            meat_list.sort()
            print('Name\t\t\tAmount\t\t\tCalories')
            print('---------------------------------------')
            for list_item in meat_list:
                name = list_item[0]
                serving = list_item[1]
                calories = list_item[2]
                print(name, '\t\t\t', serving, '\t\t\t', calories)
            print('')
            more_food = input('Would you like to perform another conversion? (y/n): ')
            print('')
            if more_food == 'y':
                continue
            else:
                print('Thanks, bye!')
                break
        if menu_choice == 3:
            veggie_list = create_separate_list(read_file, menu_choice)
            veggie_list.sort()
            print('Name\t\t\tAmount\t\t\tCalories')
            print('---------------------------------------')
            for list_item in veggie_list:
                name = list_item[0]
                serving = list_item[1]
                calories = list_item[2]
                print(name, '\t\t\t', serving, '\t\t\t', calories)
            print('')
            more_food = input('Would you like to perform another conversion? (y/n): ')
            print('')
            if more_food == 'y':
                continue
            else:
                print('Thanks, bye!')
                break
        if menu_choice == 4:
            fruit_list = create_separate_list(read_file, menu_choice)
            fruit_list.sort()
            print('Name\t\t\tAmount\t\t\tCalories')
            print('---------------------------------------')
            for list_item in fruit_list:
                name = list_item[0]
                serving = list_item[1]
                calories = list_item[2]
                print(name, '\t\t\t', serving, '\t\t\t', calories)
            print('')
            more_food = input('Would you like to perform another conversion? (y/n): ')
            print('')
            if more_food == 'y':
                continue
            else:
                print('Thanks, bye!')
                break
        if menu_choice == 5:
            grains_list = create_separate_list(read_file, menu_choice)
            grains_list.sort()
            print('Name\t\t\tAmount\t\t\tCalories')
            print('---------------------------------------')
            for list_item in grains_list:
                name = list_item[0]
                serving = list_item[1]
                calories = list_item[2]
                print(name, '\t\t\t', serving, '\t\t\t', calories)
            print('')
            more_food = input('Would you like to perform another conversion? (y/n): ')
            print('')
            if more_food == 'y':
                continue
            else:
                print('Thanks, bye!')
                break
        else: # if user enters incorrect menu selection, present error and loop through menu again
            print('Please enter a valid menu number')
            continue


# Display the menu to the user
def display_menu():
    print('Nutrition by Food Group')
    print('1. Dairy')
    print('2. Meat')
    print('3. Vegetables')
    print('4. Fruit')
    print('5. Grains')
    print('')


# Create a list of lists from the read file
def read_data():
    list_of_lists = []
    nutrition_file = open('nutrition_data.csv', 'r')  # Open the file
    info_line = nutrition_file.readline()  # Read each line of the file
    while info_line != '':  # Iterate each file line without an empty string
        read_row = info_line.rstrip('\n').split(',') # Remove newline at end of row, rows at comma
        list_of_lists.append(read_row) # Add row to empty list variable
        info_line = nutrition_file.readline() # Continue reading file to end
    nutrition_file.close() # Close file
    return list_of_lists


# Create separate lists for each of the menu options
def create_separate_list(main_list, menu_choice):
    dairy = []
    meat = []
    veggies = []
    fruit = []
    grains = []
    for list_item in main_list: # Iterate over list parameter passed
        if list_item[0] == 'Dairy': # Check list index value [0] and if it matches criteria, append to correlating list
            dairy.append(list_item[1:4])
        if list_item[0] == 'Meat':
            meat.append(list_item[1:4])
        if list_item[0] == 'Vegetables':
            veggies.append(list_item[1:4])
        if list_item[0] == 'Fruit':
            fruit.append(list_item[1:4])
        if list_item[0] == 'Grains':
            grains.append(list_item[1:4])

    if menu_choice == 1: # From passed menu option parameter, if matches criteria, return correlating updated list
        return dairy
    if menu_choice == 2:
        return meat
    if menu_choice == 3:
        return veggies
    if menu_choice == 4:
        return fruit
    if menu_choice == 5:
        return grains


main() # Call the main() function
