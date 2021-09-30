"""
Programmer: Stefanie Streger
Assignment: Module 6 - Programming Assignment
Date Completed: 9/30/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import random # Import random module

# Provide dictionary of states and capitals
states = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}


def main():
    correct = 0 # Accumulator for correct answers
    incorrect = 0 # Accumulator for incorrect answers
    state = random_state() # Run random state function into variable
    city = match_city(state) # Run matching city function into variable

    while True: # Loop for matching city and state
        user_choice = str(input('What is the capital of ' + state + '? (or enter 0 to quit): ')) # Get state capital from user
        if user_choice == city or user_choice == city.lower(): # If answer matches, regardless of case
            correct += 1 # Add count to correct answers
            state = random_state() # Get a new random city and matching state for next loop iteration
            city = match_city(state)
            print('That is correct.')
        elif user_choice != '0': # If answer is anything else but 0
            incorrect += 1 # Add count to incorrect answers
            state = random_state() # Get a new random city and matching state for next loop iteration
            city = match_city(state)
            print('That is incorrect.')
        else: # If answer is '0', end program
            print('You had', correct, 'correct responses and', incorrect, 'incorrect responses.')
            break


# Get a random state
def random_state():
    current_state = random.choice(list(states.keys()))
    return current_state


# Get a matching city to a state
def match_city(state):
    city = states.get(state)
    return city


main() # Call main program






