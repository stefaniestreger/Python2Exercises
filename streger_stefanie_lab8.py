"""
Programmer: Stefanie Streger
Assignment: Module 8 - Lab
Date Completed: 10/13/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


# Create a class for storing Pet object attributes
class Pet:
    def __init__(self, name, animal_type, age):  # Accepts params into the class
        self.__name = name  # Set hidden attributes for name, type, and age
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):  # Set pet name
        self.__name = name

    def set_animal_type(self, animal_type):  # Set pet type
        self.__animal_type = animal_type

    def set_age(self, age):  # Set pet age
        self.__age = age

    def get_name(self):  # Return pet name
        return self.__name

    def get_animal_type(self):  # Return pet type
        return self.__animal_type

    def get_age(self):  # Return pet age
        return self.__age


# Program to create instance of a pet from user input
def main():
    pet_name = str(input('What\'s the name of your pet? '))  # Ask user to provide information about their pet
    pet_type = str(input('What kind of animal is your pet? '))
    pet_age = int(input('How old is your pet? '))

    my_pet = Pet(pet_name, pet_type, pet_age)  # Create instance of pet and store user input into it

    print('=================')  # Display information about the user's pet instance
    print('Here\'s information about your pet!')
    print('')
    print('Your pet\'s name is', my_pet.get_name())
    print('The type of pet you have is a', my_pet.get_animal_type())
    print('Your pet\'s age is', my_pet.get_age())


main()  # Call the main program
