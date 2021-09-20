"""
Programmer: Stefanie Streger
Assignment: Module 4 - Lab
Date Completed: 9/14/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


def main():
    display_header() # Calls header function
    process_sales(get_quarterly_sales()) # Calls process sales function, passing quarterly sales list as a parameter


# Display the header/greeting
def display_header():
    print('The Quarterly Sales Program')


# Ask the user for input to store sales values in a list as float values
def get_quarterly_sales():
    sales_list = []
    first_quarter = float(input('Enter sales for Q1: '))
    sales_list.append(first_quarter)
    second_quarter = float(input('Enter sales for Q2: '))
    sales_list.append(second_quarter)
    third_quarter = float(input('Enter sales for Q3: '))
    sales_list.append(third_quarter)
    fourth_quarter = float(input('Enter sales for Q4: '))
    sales_list.append(fourth_quarter)

    return sales_list


# Calculates math needs from a list of values
def process_sales(list_values):
    total_sales = 0
    for value in list_values:
        total_sales += value

    average = total_sales / len(list_values)

    print('')
    print('Total: $', format(total_sales, '.2f'))
    print('Average Quarter: $', format(average, '.2f'))
    print('Lowest Quarter: $', format(min(list_values), '.2f'))
    print('Highest Quarter: $', format(max(list_values), '.2f'))


main() # Calls the main function
