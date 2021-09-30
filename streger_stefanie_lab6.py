"""
Programmer: Stefanie Streger
Assignment: Module 6 - Lab
Date Completed: 9/28/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


def main():
    start_file = open('first_file.txt', 'r') # Open first file in read mode
    start_file_line = start_file.read().replace(',', '') # Read the file and remove commas
    list_one = start_file_line.rstrip('\n').split() # Remove newline char and separate each word in string
    start_file.close() # Close the file

    next_file = open('second_file.txt', 'r') # Open second file in read mode
    next_file_line = next_file.read().replace(',', '') # Read the file and remove commas
    list_two = next_file_line.rstrip('\n').split() # Remove newline char and separate each word in string
    next_file.close() # Close the file

    unique_words(list_one, list_two) # Begin running all functions defined for output, pass lists created above as params
    print('')
    shared_words(list_one, list_two)
    print('')
    unique_first_file_words(list_one, list_two)
    print('')
    unique_second_file_words(list_one, list_two)
    print('')
    unique_unshared_words(list_one, list_two)
    print('')


# Function to compare two lists and show unique words in both files
def unique_words(list1, list2):
    set_one = set(list1) # Create list 1 param as an immutable set
    set_two = set(list2) # Create list 2 param as an immutable set
    set_three = set_one.intersection(set_two)  # Find words that appear in both files
    print('The unique words that appear in both files are:', set_three)


# Function to compare two lists and show words that appear in both files
def shared_words(list1, list2):
    set_one = set(list1)
    set_two = set(list2)
    set_three = set_one.union(set_two)
    print('The words that appear in both files are:', set_three)


# Function to compare two lists and show words in first file, but not in second
def unique_first_file_words(list1, list2):
    set_one = set(list1)
    set_two = set(list2)
    set_three = set_one.difference(set_two)
    print('The words that appear in the first file, but not in the second file are:', set_three)


# Function to compare two lists and show words that appear in second file, but not in first
def unique_second_file_words(list1, list2):
    set_one = set(list1)
    set_two = set(list2)
    set_three = set_two.difference(set_one)
    print('The words that appear in the second file, but not in the first file are:', set_three)


# Function to compare two lists and show words that appear in either file, but not in both
def unique_unshared_words(list1, list2):
    set_one = set(list1)
    set_two = set(list2)
    set_three = set_one.symmetric_difference(set_two)
    print('The words that appear in either the first or second file, but not both are:', set_three)


main() # Call main() function
