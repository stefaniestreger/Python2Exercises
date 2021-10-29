"""
Programmer: Stefanie Streger
Assignment: Module 8 - Programming Assignment - Employee File
Date Completed: 10/13/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

# Create a class for Employee with attributes
class Employee:

    def __init__(self, name, id_number, department, job_title): # Initialize attributes for class
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):  # Set name for object instance
        self.__name = name

    def set_id_number(self, id_number):  # Set id for object instance
        self.__id_number = id_number

    def set_department(self, department):  # Set dept for object instance
        self.__department = department

    def set_job_title(self, job_title):  # Set job title for object instance
        self.__job_title = job_title

    def get_name(self):  # Return name for object instance
        return self.__name

    def get_id_number(self):  # Return id for object instance
        return self.__id_number

    def get_department(self):  # Return dept for object instance
        return self.__department

    def get_job_title(self):  # Return title for object instance
        return self.__job_title

    def __str__(self): # Returns object state
        return '\nName: ' + self.__name + \
               '\nID Number: ' + self.__id_number + \
               '\nDepartment: ' + self.__department + \
               '\nTitle: ' + self.__job_title
