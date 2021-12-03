"""
Programmer: Stefanie Streger
Assignment: Module 12 - Lab
Date Completed: 11/11/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


# Create function for print_lines
def print_lines(n):
    print('Recursion ' + str(n)) # Print recursion text with passed param converted to string
    if n > 1: # if param is greater than 1
        print_lines(n - 1) # recursively call function and subtract 1 every time it's called

    if n == user_value: # once the param is same value as input value
        for item in range(n): # loop through range of parameter value
            print('*' * (item + 1), end='\n') # print asterisk on a line for every


user_value = int(input('How many lines to display? ')) # ask for user input to set value to pass to function

print_lines(user_value) # call print_lines function with user_value param passed to it 
