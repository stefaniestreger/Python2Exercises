"""
Programmer: Stefanie Streger
Assignment: Module 14 - Programming Assignment
Date Completed: 11/24/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""

import tkinter # Import library


class StateFlag: # Create class for state flag of TN
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, width=500, height=300)
        self.canvas.create_rectangle(20, 20, 460, 280, fill='#BA0101') # red part of flag
        self.canvas.create_rectangle(461, 20, 465, 280, fill='#FFFFFF') # white divider
        self.canvas.create_rectangle(466, 20, 495, 280, fill='#003366') # blue part of flag
        self.canvas.create_oval(160, 50, 330, 220, fill='#FFFFFF') # outer white circle
        self.canvas.create_oval(165, 55, 325, 215, fill='#003366') # inner white circle
        self.canvas.create_polygon(205, 145, 225, 175, 185, 155, 225, 155, 195, 175, 205, 145, fill='#FFFFFF') # star 1 in bottom left quadrand
        self.canvas.create_polygon(215, 85, 225, 115, 195, 95, 235, 95, 205, 115, 215, 85, fill='#FFFFFF') # star 2 in top left quadrant
        self.canvas.create_polygon(275, 115, 295, 145, 255, 125, 295, 125, 265, 145, 275, 115, fill='#FFFFFF') # star 3 in middle right quadrant

        self.canvas.pack()
        tkinter.mainloop()


my_flag = StateFlag() 
