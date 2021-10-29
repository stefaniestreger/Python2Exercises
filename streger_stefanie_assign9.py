"""
Programmer: Stefanie Streger
Assignment: Module 9 - Programming Assignment
Date Completed: 10/21/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import emp # Import the employee module


# Create main program
def main():
    name = str(input('Enter the name: ')) # Ask user for input and save to variables
    id = int(input('Enter the ID number: '))
    salary = int(input('Enter the annual salary: '))
    bonus = int(input('Enter the bonus: '))

    supervisor = emp.ShiftSupervisor(name, id, salary, bonus) # Pass supervisor information into variable for the subclass

    print('') # Print results from created variable
    print('Shift supervisor worker information: ')
    print('Name: ', supervisor.get_name())
    print('ID number: ', supervisor.get_id())
    print('Annual Salary: ', format(supervisor.get_salary(), ',.2f'))
    print('Annual Production Bonus: $', format(supervisor.get_bonus(), ',.2f'))


main() # Call the main function
