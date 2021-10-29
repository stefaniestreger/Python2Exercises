"""
Programmer: Stefanie Streger
Assignment: Module 8 - Programming Assignment
Date Completed: 10/13/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import emp # Import the emp.py file


def main():

    emp_one_name = 'Susan Meyers' # Set variables for first instance
    emp_one_number = '47899'
    emp_one_dept = 'Accounting'
    emp_one_title = 'Vice President'

    emp_one = emp.Employee(emp_one_name, emp_one_number)  # Create instance for employee 1

    emp_two_name = 'Mark Jones' # Set variables for second instance
    emp_two_number = '39119'
    emp_two_dept = 'IT'
    emp_two_title = 'Programmer'

    emp_two = emp.Employee(emp_two_name, emp_two_number)  # Create instance for employee 2

    emp_three_name = 'Joy Rogers' # Set variables for thier instance
    emp_three_number = '81774'
    emp_three_dept = 'Manufacturing'
    emp_three_title = 'Engineer'

    emp_three = emp.Employee(emp_three_name, emp_three_number)  # Create instance for employee 3

    print('Employee 1:', emp_one) # Print object instance for emp 1
    print('')
    print('Employee 2:', emp_two) # Print object instance for emp 2
    print('')
    print('Employee 3:', emp_three) # Print object instance for emp 3


main() # Call the main function