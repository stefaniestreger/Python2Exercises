"""
Programmer: Stefanie Streger
Assignment: Module 10 - Lab
Date Completed: 10/27/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


class SimpleCounter: # Create super class from instructions
    def __init__(self, firstnum):
        self.__count = firstnum

    def increment(self):
        self.__count += 1

    def clear(self):
        self.__count = 0

    def get_value(self):
        return self.__count

    def decrement(self):
        pass


class AdvancedCounter(SimpleCounter): # Create subclass from superclass
    def __init__(self, secondnum): # Initialize the subclass
        super().__init__(secondnum) # Initialize from the superclass
        self.__count = secondnum

    def increment(self): # Method to increment by 2
        self.__count += 2

    def decrement(self): # Method to decrement by 1
        self.__count -= 1

    def clear(self): # Method to clear count to 0
        self.__count = 0

    def get_value(self): # Method to return current count (whatever it is)
        return self.__count


def main(): # Define the main program

    user_num = int(input('Add an initial number: ')) # Get a number from the user

    simple_count = SimpleCounter(user_num) # Create object for superclass
    adv_count = AdvancedCounter(user_num) # Create object for subclass

    print('')
    print('After incrementing...')
    simple_count.increment() # Increment input from user
    adv_count.increment()
    print(simple_count.get_value()) # Print incremented values
    print(adv_count.get_value())

    print('')
    print('After decrementing...')
    simple_count.decrement() # Decrement input from user
    adv_count.decrement()
    print(simple_count.get_value()) # Print decremented values
    print(adv_count.get_value())

    print('')
    print('After clearing...')
    simple_count.clear() # Clear input from user
    adv_count.clear()
    print(simple_count.get_value()) # Print cleared values
    print(adv_count.get_value())


main() # Call the main function
