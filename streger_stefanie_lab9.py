"""
Programmer: Stefanie Streger
Assignment: Module 9 - Lab
Date Completed: 10/21/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import emp # Import the employee module


# Create main program
def main():
    name = str(input('Enter the name: ')) # Ask user for input and save to variables
    id = int(input('Enter the ID number: '))
    shift = int(input('Enter the shift number: '))
    hourly_pay = int(input('Enter the hourly pay rate: '))

    worker = emp.ProductionWorker(name, id, shift, hourly_pay) # Pass worker information into variable for the subclass

    print('') # Print results from created variable
    print('Production worker information: ')
    print('Name: ', worker.get_name())
    print('ID number: ', worker.get_id())
    print('Shift: ', worker.get_shift())
    print('Hourly Pay Rate: $', format(worker.get_hourly_pay(), '.2f'))


main() # Call the main function
