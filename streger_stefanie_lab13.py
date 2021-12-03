"""
Programmer: Stefanie Streger
Assignment: Module 13 - Lab
Date Completed: 11/18/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


import tkinter # Import tkinter library


class Show_Info: # Create class to show information
    def __init__(self): # Define the class
        self.main_window = tkinter.Tk() # Create the main window
        self.canvas = tkinter.Canvas(self.main_window, width=100, height=50) # Use Canvas widget to specify dimensions for the window
        self.top_frame = tkinter.Frame(self.main_window) # Create top and bottom frames for GUI
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.value = tkinter.StringVar() # Associate string variable for address value to a label
        self.address_label = tkinter.Label(self.top_frame, textvariable=self.value)
        self.address_label.pack(side='top') # Set address label at top of frame
        self.show_info = tkinter.Button(self.bottom_frame, text='Show Info', command=self.my_info) # Create button to Show Info in bottom frame with call to function for my info
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit', command=self.main_window.destroy) # Create exit button in bottom frame with callback function
        self.top_frame.pack() # Pack the top frame first
        self.canvas.pack()  # Pack the canvas widget next
        self.show_info.pack(side='left')  # Pack buttons in frame to left showing Show Info first
        self.exit_button.pack(side='left')
        self.bottom_frame.pack() # Pack bottom frame last
        tkinter.mainloop() # Start the main loop for GUI

    def my_info(self): # Create function to display my information
        self.value.set('\nStefanie Streger' +
                       '\n147 Walton Trace S.' +
                       '\nHendersonville' + ', ' + 'TN' + '  ' + '37075')


my_info = Show_Info() # Create an instance of the Show_Info class 
