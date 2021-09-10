"""
Programmer: Stefanie Streger
Assignment: Module 3 - Programming Assignment
Date Completed: 9/9/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


def main():
    print('Contact Manager')
    print()
    contacts_file = str(input('Enter Contacts File Name: ')) # Ask user for a file to open

    while True:
        try: # Try opening file and display menu
            read_file = open(contacts_file, 'r')
            display_menu()
            break

        except FileNotFoundError as e: # If file name incorrect or doesn't exist, throw error
            print('File name is invalid or does not exist')
            contacts_file = str(input('Enter Contacts File Name: ')) # Ask user for new file name
            continue # Continue loop until a valid file name is entered

    menu_option = str(input('Command: '))  # Ask user to enter a menu option
    while True:
        if menu_option == 'view':
            view_contacts(contacts_file) # If menu option view, run view function
        elif menu_option == 'add':
            add_contacts(contacts_file) # If menu option add, run add function
        elif menu_option == 'del':
            delete_contacts(contacts_file) # If menu option delete, run delete function
        elif menu_option == 'exit':
            print('Bye!') # If menu option exit, end program and break
            break
        else:
            print('You did not enter a correct menu option. Please enter a valid choice')
        menu_option = str(input('Command: ')) # Any other menu option, ask user to enter a different menu option
        continue # Continue until user enters a valid menu option


# Display the menu to the user
def display_menu():
    print('COMMAND MENU')
    print('view - View a contact')
    print('add - Add a contact')
    print('del - Delete a contact')
    print('exit - Exit program')
    print()


# Display contacts in file to user
def view_contacts(contact_file):
    view_file = open(contact_file, 'r')
    contact_row = view_file.readline()
    counter = 0
    while contact_row != '':
        for line in contact_row: # Loops over accumulator and increments the counter by 1
            counter += 1
            print(str(counter) + '. ' + contact_row) # Prints each line in the file
            break
        contact_row = view_file.readline()
    view_file.close() # Close file
    display_menu() # Display the menu to the user


# Add new contact to the contact file
def add_contacts(contact_file):
    name = str(input('Name: ')) # Save name, email and phone to variables from user input
    email = str(input('Email: '))
    phone = str(input('Phone: '))

    contacts_file = open(contact_file, 'a')
    contacts_file.write(name + ', ' + email + ', ' + phone + '\n') # Write contact to file at bottom of list

    print(name, 'was added.')
    print()

    display_menu() # Display the menu to the user


# Delete contact from the contact file
def delete_contacts(contact_file):
    view_contacts(contact_file) # Show file contents to user
    delete_option = int(input('Enter the number of the contact to delete: ')) # Ask user for number of contact to delete

    contacts_file = open(contact_file, 'r') # Read file
    view_line = contacts_file.readline()
    counter = 0
    saved_items = [] # Function variable for contacts user doesn't want to delete
    while view_line != '':
        for line in view_line: # Loops over accumulator and increments the counter by 1
            counter += 1
            break

        if counter != delete_option: # Compare user option with counter value
            saved_items.append(view_line) # Append line being read to variable
        view_line = contacts_file.readline()
    contacts_file.close()

    update_file = open(contact_file, 'w') # Open file in write mode
    for contact in saved_items: # Loop through variable and write each item back to the file
        update_file.write(str(contact))
    update_file.close()
    print(delete_option, ' was removed')

    display_menu() # Display the menu to the user


main()
