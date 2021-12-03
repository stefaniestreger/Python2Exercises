"""
Programmer: Stefanie Streger
Assignment: Module 14 - Lab
Date Completed: 11/24/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import tkinter # Import libaries
import tkinter.messagebox


class Automotive: # Create class
    def __init__(self):  # Initialize the class with frames
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width=100,
                                     height=50)
        self.menu_choices = tkinter.Frame(self.main_window)
        self.car_wash = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Add checkboxes in GUI
        self.oil_change = tkinter.IntVar()
        self.lube_job = tkinter.IntVar()
        self.radiator_flush = tkinter.IntVar()
        self.transmission_flush = tkinter.IntVar()
        self.inspection = tkinter.IntVar()
        self.muffler_replace = tkinter.IntVar()
        self.tire_rotation = tkinter.IntVar()
        self.oil_change.set(0)
        self.lube_job.set(0)
        self.radiator_flush.set(0)
        self.transmission_flush.set(0)
        self.inspection.set(0)
        self.muffler_replace.set(0)
        self.tire_rotation.set(0)
        self.cb1 = tkinter.Checkbutton(self.menu_choices, text='Oil Change - $30.00', variable=self.oil_change)
        self.cb2 = tkinter.Checkbutton(self.menu_choices, text='Lube Job - $20.00', variable=self.lube_job)
        self.cb3 = tkinter.Checkbutton(self.menu_choices, text='Radiator Flush - $40.00', variable=self.radiator_flush)
        self.cb4 = tkinter.Checkbutton(self.menu_choices, text='Transmission Flush - $100.00',
                                       variable=self.transmission_flush)
        self.cb5 = tkinter.Checkbutton(self.menu_choices, text='Inspection - $35.00', variable=self.inspection)
        self.cb6 = tkinter.Checkbutton(self.menu_choices, text='Muffler Replacement - $200.00',
                                       variable=self.muffler_replace)
        self.cb7 = tkinter.Checkbutton(self.menu_choices, text='Tire Rotation - $20.00', variable=self.tire_rotation)
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Add radio buttons in GUI
        self.car_wash_label = tkinter.Label(self.car_wash, text='Would You like A Car Wash?')
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1) # This will set default selection to Yes rather than none, which is what I want
        self.rb1 = tkinter.Radiobutton(self.car_wash, text='Yes', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.car_wash, text='No', variable=self.radio_var, value=2)
        self.car_wash_label.pack()
        self.rb1.pack()
        self.rb2.pack()

        # Add function buttons in GUI
        self.display_charges = tkinter.Button(self.button_frame, text='Display Charges',
                                              command=self.display_charges)
        self.quit = tkinter.Button(self.button_frame, text='Quit',
                                   command=self.main_window.destroy)
        self.display_charges.pack(side='left')
        self.quit.pack(side='left')

        # Pack GUI frames
        self.menu_choices.pack()
        self.car_wash.pack()
        self.canvas.pack()
        self.button_frame.pack()

        tkinter.mainloop()  # Start the main loop for GUI

# Create function for calculating charges and car wash selection
    def display_charges(self):
        self.total_price = 0
        self.oil_price = 30
        self.lube_price = 20
        self.radiator_price = 40
        self.transmission_price = 100
        self.inspection_price = 35
        self.muffler_price = 30
        self.tire_rotate = 30
        if self.oil_change.get() == 1:
            self.total_price += self.oil_price
        if self.lube_job.get() == 1:
            self.total_price += self.lube_price
        if self.radiator_flush.get() == 1:
            self.total_price += self.radiator_price
        if self.transmission_flush.get() == 1:
            self.total_price += self.transmission_price
        if self.inspection.get() == 1:
            self.total_price += self.inspection_price
        if self.muffler_replace.get() == 1:
            self.total_price += self.muffler_price
        if self.tire_rotation.get() == 1:
            self.total_price += self.tire_rotate
        if self.radio_var.get() == 1:
            self.car_wash = 'accepted.'
        else:
            self.car_wash = 'declined.'

        self.message = f'Your total charges = ${self.total_price}\n\nFree car wash was ' + self.car_wash
        tkinter.messagebox.showinfo('Total Charges', self.message)


# Create an instance of the Automotive class
user_choices = Automotive()
