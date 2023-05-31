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
    
'''May 18th: I created labels'''
#creating the labels (entries)
           #these are the global variables that are used, accessible throughout the program
    global hire_details, entry_name,entry_receiptnumber,entry_item,entry_numberhired, total_entries, delete_item
    #customer name
    Label(main_window, text="Customer Full Name",font='Georgia 18') .grid(column=0,row=2,padx=20)
    entry_name = Entry(main_window,font='Georgia 16')
    entry_name.grid(column=1,row=2,padx=10,pady=5)
    #receipt number
    Label(main_window, text="Receipt Number",font='Georgia 18') .grid(column=0,row=3)
    entry_receiptnumber = Entry(main_window,font='Georgia 16')
    entry_receiptnumber.grid(column=1,row=3,padx=10,pady=5)
    #item hired (combobox)
    item_hired = StringVar()
    Label(main_window, text="Item Hired",font='Georgia 18') .grid(column=0,row=4)
    entry_item = ttk.Combobox(main_window,font='Georgia 16', textvariable=item_hired, values=('Cutlery Set', 'Glassware','Chairs', 'Tables', 'Balloons', 'Booth hire',
                                                                            'Prop hire','Jukebox','Party lights', 'Dance floor'), state='readonly')
    entry_item.grid(column=1,row=4,padx=10,pady=5)                                                 
    #number hired
    Label(main_window, text="Quantity Hired",font='Georgia 18') .grid(column=0,row=5)
    entry_numberhired = Entry(main_window,font='Georgia 16')
    entry_numberhired.grid(column=1,row=5,padx=10,pady=5)
    #row number (for when item is returned)
    Label(main_window, text="Row #",font='Georgia 18') .grid(column=0,row=6)
    delete_item = Entry(main_window,font='Georgia 16')
    delete_item .grid(column=1,row=6,padx=10,pady=5)






