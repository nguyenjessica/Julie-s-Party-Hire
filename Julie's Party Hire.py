'''Jessica Nguyen Julie's Party Hire
Today, May 17th, I began to code.'''
#import tkinter library
rom tkinter import *
from tkinter import ttk
from tkinter import messagebox
 
'''----------------------------------------- Set up GUI -----------------------------------------
Create the title, default buttons, labels, and entry boxes. Put them in the correct grid location.'''

#create the buttons and title
    #buttons: update(append),print,delete(row),quit

def setup_buttons():
    Button(main_window, text="Update",font="Georgia 15", bg="#FFD7D7", highlightbackground="#FFD7D7",command=check_inputs) .grid(column=0,row=1,sticky=E,ipadx=20,ipady=5,pady=5)
    Button(main_window, text="Print",font="Georgia 15", bg="#FFD7D7", highlightbackground="#FFD7D7", command=print_hire_details) .grid(column=1,row=1,ipadx=20,ipady=5,pady=5)
    Button(main_window, text="Quit",font="Georgia 15", bg="#FFD7D7", highlightbackground="#FFD7D7", command=quit,width=5) .grid(column=2,row=1,sticky=W,ipadx=20,ipady=5,pady=5)
    Button(main_window, text="Delete",font="Georgia 15", bg="#FFD7D7", highlightbackground="#FFD7D7", command=delete_row) .grid(column=2,row=6,sticky=W,ipadx=20,ipady=3)
    #title
    Label(main_window, text = "Julie's Party Hire", font="Georgia 25", bg="#FFD7D7").grid(column=1,row=0,pady=(30,10))






