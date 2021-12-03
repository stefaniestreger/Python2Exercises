"""
Programmer: Stefanie Streger
Assignment: Module 12 - Programming Assignment
Date Completed: 11/11/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


# Create function for recursive algorithm to find GCD
def find_gcd(num1, num2): # Accepts 2 numbers
    if num1 % num2 == 0: # Get the remainder of the two numbers; if remainder = 0
        return num2 # Return value of num2
    else:
        return find_gcd(num1, num1 % num2) # Otherwise call recursive function and pass num1, and remainder as params


# Create program to find GCD of input numbers
def main():
    print('Greatest Common Divisor:')

    while True: # Loop while true
        num1 = int(input('Enter Number 1: ')) # Ask user for num1 value
        num2 = int(input('Enter Number 2: ')) # Ask user for num2 value

        if num1 < num2: # If num 1 less than num2, print message
            print('First number must be greater than second number')
        else:
            gcd = find_gcd(num1, num2) # Call function and pass user input values
            print('Greatest common divisor: ', gcd) # Print message with gcd from function
            keep_going = str(input('Continue? (y/n): ')) # Ask user to continue
            if keep_going == 'y': # If yes continue, loop through again
                continue
            else: # Otherwise, end program
                print('Bye!')
                break


main() # Call main function
