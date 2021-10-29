# Create a class for Employee with attributes
class Employee:

    def __init__(self, name, id):  # Initialize attributes for class
        self.__name = name
        self.__id = id

    def set_name(self, name):  # Set name for object instance
        self.__name = name

    def set_id(self, id):  # Set id for object instance
        self.__id = id

    def get_name(self):  # Return name for object instance
        return self.__name

    def get_id(self):  # Return id for object instance
        return self.__id


# Create subclass of the Employee class - ProductionWorker
class ProductionWorker(Employee):
    def __init__(self, name, id, shift, hourly_pay):  # Initialize attributes for super- and subclass
        Employee.__init__(self, name, id) # Initialize attributes for superclass
        self.__shift = shift
        self.__hourly_pay = hourly_pay

    def set_shift(self, shift):  # Set name for object instance
        self.__shift = shift

    def set_hourly_pay(self, hourly_pay):  # Set id for object instance
        self.__hourly_pay = hourly_pay

    def get_shift(self):  # Return name for object instance
        return self.__shift

    def get_hourly_pay(self):  # Return id for object instance
        return self.__hourly_pay


# Create subclass of the Employee class - ShiftSupervisor
class ShiftSupervisor(Employee):
    def __init__(self, name, id, salary, bonus):  # Initialize attributes for super- and subclass
        Employee.__init__(self, name, id) # Initialize attributes for superclass
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):  # Set name for object instance
        self.__salary = salary

    def set_bonus(self, bonus):  # Set id for object instance
        self.__bonus = bonus

    def get_salary(self):  # Return name for object instance
        return self.__salary

    def get_bonus(self):  # Return id for object instance
        return self.__bonus
