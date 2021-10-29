"""
Programmer: Stefanie Streger
Assignment: Module 10 - Programming Assignment
Date Completed: 10/27/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


# Create a superclass for Person with attributes
class Person:

    def __init__(self, firstname, lastname, email):  # Initialize attributes for superclass
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email

    def set_firstname(self, firstname):  # Set firstname for object instance
        self.__firstname = firstname

    def set_lastname(self, lastname):  # Set lastname for object instance
        self.__lastname = lastname

    def set_email(self, email):  # Set email for object instance
        self.__email = email

    def get_firstname(self):  # Return firstname for object instance
        return self.__firstname

    def get_lastname(self):  # Return lastname for object instance
        return self.__lastname

    def get_email(self):  # Return email for object instance
        return self.__email

    def get_information(self):  # Placeholder for information method
        pass


# Create subclass of the Person class - Customer
class Customer(Person):
    def __init__(self, firstname, lastname, email, customer_number):  # Initialize attributes for super- and subclass
        super().__init__(firstname, lastname, email)  # Initialize attributes for superclass
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__customer_number = customer_number  # Include new attribute for customer number

    def set_firstname(self, firstname):  # Set firstname for object instance
        self.__firstname = firstname

    def set_lastname(self, lastname):  # Set lastname for object instance
        self.__lastname = lastname

    def set_email(self, email):  # Set email for object instance
        self.__email = email

    def set_customer_number(self, customer_number):  # Set customer number for object instance
        self.__customer_number = customer_number

    def get_firstname(self):  # Return firstname for object instance
        return self.__firstname

    def get_lastname(self):  # Return lastname for object instance
        return self.__lastname

    def get_email(self):  # Return email for object instance
        return self.__email

    def get_number(self):  # Return customer number for object instance
        return self.__customer_number

    def get_information(self):  # Method for all customer information
        return '\nCustomer: ' + self.__firstname + '\t' + self.__lastname + \
               '\nCustomer Email: ' + self.__email + \
               '\nCustomer Number: ' + self.__customer_number


# Create subclass of the Person class - Employee
class Employee(Person):
    def __init__(self, firstname, lastname, email, emp_social):  # Initialize attributes for super- and subclass
        super().__init__(firstname, lastname, email)  # Initialize attributes for superclass
        self.__firstname = firstname
        self.__lastname = lastname
        self.__email = email
        self.__emp_social = emp_social  # Include new attribute for social

    def set_firstname(self, firstname):  # Set firstname for object instance
        self.__firstname = firstname

    def set_lastname(self, lastname):  # Set lastname for object instance
        self.__lastname = lastname

    def set_email(self, email):  # Set email for object instance
        self.__email = email

    def set_social(self, emp_social):  # Set social for object instance
        self.__emp_social = emp_social

    def get_information(self):  # Method for all employee information
        return '\nEmployee: ' + self.__firstname + '\t' + self.__lastname + \
               '\nEmployee Email: ' + self.__email + \
               '\nEmployee Number: ' + self.__emp_social


def display(value):  # Function to display values in get_information methods in both subclasses
    if isinstance(value, Customer):
        print('CUSTOMER INFORMATION')
        print(Customer.get_information(value))
    else:
        print('EMPLOYEE INFORMATION')
        print(Employee.get_information(value))


def main(): # Define the main function
    print('Customer/Employee Data Entry')
    while True: # Ask customer for input about person
        first_name = str(input('First Name: '))
        last_name = str(input('Last Name: '))
        email = str(input('Email: '))
        user_choice = str(input('Customer or employee? (c/e): ')) # Ask customer if customer or employee
        if user_choice == 'c': # If customer, ask for customer number
            number = str(input('Number: '))
            customer = Customer(first_name, last_name, email, number) # Create instance of customer
            print('')
            display(customer) # Call display method for customer instance
            keep_going = str(input('Continue? (y/n): ')) # Ask user to keep going
            if keep_going == 'y': # If continue is yes, loop again
                continue
            else:
                print('Bye!') # If continue is no, end
                break

        if user_choice == 'e': # If employee, ask for social
            social = str(input('SSN: '))
            employee = Employee(first_name, last_name, email, social) # Create instance of employee
            print('')
            display(employee) # Call display method for employee instance
            keep_going = str(input('Continue? (y/n): ')) # Ask user to keep going
            if keep_going == 'y': # If continue is yes, loop again
                continue
            else: # If continue is no, end
                print('Bye!')
                break


main() # Call the main function
