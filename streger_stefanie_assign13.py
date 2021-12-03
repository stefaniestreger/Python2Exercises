"""
Programmer: Stefanie Streger
Assignment: Module 13 - Programming Assignment
Date Completed: 11/18/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import tkinter # Import tkinter library


class Miles_Per_Gallon: # Create class for MPG GUI
    def __init__(self): # Initialize the class
        self.main_window = tkinter.Tk()  # Create the main window
        self.canvas = tkinter.Canvas(self.main_window, width=100,
                                     height=50)  # Use Canvas widget to specify dimensions for the window
        self.number_gallons_frame = tkinter.Frame(self.main_window) # Add frames needed in GUI for entry, result, and buttons
        self.number_miles_frame = tkinter.Frame(self.main_window)
        self.miles_per_gallon_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Code to add a Number of Gallons label and entry box in GUI
        self.gas_gallons_label = tkinter.Label(self.number_gallons_frame, text='Number of gallons of gas the car holds:')
        self.gas_gallons_entry = tkinter.Entry(self.number_gallons_frame, width=10)
        self.gas_gallons_label.pack(side='left')
        self.gas_gallons_entry.pack(side='left')

        # Code to add a Number of Miles label and entry box in GUI
        self.number_miles_label = tkinter.Label(self.number_miles_frame, text='Number of miles driven on a full tank:')
        self.number_miles_entry = tkinter.Entry(self.number_miles_frame, width=10)
        self.number_miles_label.pack(side='left')
        self.number_miles_entry.pack(side='left')

        # Code to add an Average label and set the variable in the GUI
        self.average_result_label = tkinter.Label(self.miles_per_gallon_frame, text='Number of miles driven per gallon of gas:')
        self.average_mpg = tkinter.StringVar()
        self.average_mpg_label = tkinter.Label(self.miles_per_gallon_frame, textvariable=self.average_mpg)
        self.average_result_label.pack(side='left')
        self.average_mpg_label.pack(side='left')

        # Code to add buttons for functions in GUI
        self.calculate_mpg = tkinter.Button(self.button_frame, text='Calculate MPG', command=self.mpg)  # Create button to Calculate MPG with call to function
        self.exit_button = tkinter.Button(self.button_frame, text='Exit',
                                          command=self.main_window.destroy)  # Create exit button with callback function
        self.calculate_mpg.pack(side='left')  # Pack buttons in frame to left showing Calculate first
        self.exit_button.pack(side='left')

        # Code to pack GUI frames
        self.number_gallons_frame.pack()
        self.number_miles_frame.pack()
        self.miles_per_gallon_frame.pack()
        self.canvas.pack()
        self.button_frame.pack()

        tkinter.mainloop()  # Start the main loop for GUI

    def mpg(self): # Create function to calculate miles per gallon from user entry
        self.gallons = int(self.gas_gallons_entry.get())
        self.miles = int(self.number_miles_entry.get())
        self.average = self.miles / self.gallons
        self.average_mpg.set(self.average) # Set result to StringVar in class


avg_mpg = Miles_Per_Gallon()   # Create an instance of the Miles_Per_Gallon class
