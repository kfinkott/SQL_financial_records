#scr_gui.py
#kevin fink
#kevin@shorecode.org
#Oct 7 2023

import logging
import tkinter as tk
from tkinter import ttk
import scr_logging
import scr_sql_tasks
from dataclasses import dataclass
from ttkthemes import ThemedStyle

@dataclass
class ScrGui:
    # Start the logger, filename scr.log
    logger = scr_logging.set_logging('scr', 'scr.log')
    
    def create_root(self):
        """
        Creates the main GUI window and starts the gui loop
        
        Args:
        self ( _obj_ ) : Parent class object
        
        Returns:
        Does not return
        """
        
        self.logger.info('Creating main window, running main loop')        
        # Create the main window
        root = tk.Tk()
        # Creates the four main buttons and sets their command   
        self.start_gui(root)
        # Start the Tkinter event loop
        root.mainloop()

    def open_window(self, category, root):
        """
        Opens the secondary text input form window
        
        Args:
        self ( _obj_ ) : Parent class object
        category ( _obj_ ) : Transaction category 
        root ( _obj_ ) : Main GUI window object
        
        Returns:
        Does not return
        """
        # Create a new window
        self.logger.info('New text input window created')
        self.new_window = tk.Toplevel(root)
        self.new_window.title(category)
        self.new_window.bind('<Return>', self.enterKeyPress)
    
        # Create six text entry boxes]
        text_box_names = ['Amount', 'Currency', 'TaxAmount', 'Date', 'Description', 'Party']
        input_boxes = []
        
        self.logger.info('Creating input boxes')    
        for i in range(len(text_box_names)):
            # Currency is the index 1. The if statement adds a default value of USD to the text box
            if i == 1:
                input_boxes.append(self.create_submit_form(text_box_names[i], default_text='USD'))
            # Date is the index 3. The if statement adds a default value of
            #2023-MM-DD to the text box
            elif i == 3:
                input_boxes.append(self.create_submit_form(text_box_names[i], default_text='2023-MM-DD'))
            else:
                input_boxes.append(self.create_submit_form(text_box_names[i], default_text=None))
    
        # Draws all the text boxes to the window
        for i in range(len(input_boxes)):
            # Label
            input_boxes[i][0].pack()
            # Text entry box
            input_boxes[i][1].pack()

        # A submit button to transfer all the user inputted text entry data. also closed the text
        # entry window.
        self.logger.info('Creating submit button')
        self.submit_button = tk.Button(self.new_window, text="Submit", command=lambda: [self.to_sql(
                self.get_entries(input_boxes), text_box_names, category), self.new_window.destroy(),
                self.logger.info('Sumit button pressed, transfering data to SQL')])
        self.submit_button.pack()
    
    def create_submit_form(self, title, default_text=None):
        """
        Creates a label widget and a text input box widget
        
        Args:
        self ( _obj_ ) : Parent class object
        title ( _obj_ ) : Description for the text input box
        default_text=None ( _obj_ ) : Default text to be added to the text input box
        
        Returns:
        Does not return
        """
    
        label = tk.Label(self.new_window, text=f"{title}: ")
        entry = tk.Entry(self.new_window, background='orange')
    
        # Enters the default text for the field if it is provided
        if default_text is not None:
            entry.insert(0, default_text)
        return label, entry

    def enterKeyPress(self, event):
        """
        Function that defines the logic to be executed when the enter key is pressed
        
        Args:
        self ( _obj_ ) : Parent class object
        event ( _obj_ ) : Not used
        
        Returns:
        DOes not return
        """
        # Presses the submit button
        self.submit_button.invoke()
        # Closes the text input form window
        self.new_window.destroy()
        self.logger.info('Enter key pressed, transfering data to SQL')

    def get_entries(self, input_boxes):
        """
        Collects the text input from every input box in the window
        
        Args:
        self ( _obj_ ) : Parent class object
        input_boxes ( _obj_ ) : List containing all the text input boxes and their labels
        
        Returns:
        Does not return
        """
        entries = []
        # Collects all the text entry from all the input boxes
        self.logger.info('Collecting user text input')
        for i in range(len(input_boxes)):
            entries.append(input_boxes[i][1].get())
        return entries

    def start_gui(self, root):
        """
        Sets the title for the main window and creates all the buttons for the main menu
        
        Args:
        self ( _obj_ ) : Parent class object
        root ( _obj_ ) : Main window object
        
        Returns:
        Does not return
        """
    
        self.logger.info('Gui module starting')
        self.logger.info('*'*100)
    
        # Sets the title for the main window
        root.title("Main Window")
    
        # Create four buttons. Calls a new text entry window when pressed.
        button_names = ['Income record', 'Expense record', 'Investment purchase', 'Investment sale']
        self.logger.info('Creating main menu buttons')
        inc_button = tk.Button(root, text=button_names[0], command=lambda: self.open_window(
            button_names[0], root), width=45)
        inc_button.pack()
        exp_button = tk.Button(root, text=button_names[1], command=lambda: self.open_window(
            button_names[1], root), width=45)
        exp_button.pack()
        invp_button = tk.Button(root, text=button_names[2], command=lambda: self.open_window(
            button_names[2], root), width=45)
        invp_button.pack()
        invs_button = tk.Button(root, text=button_names[3], command=lambda: self.open_window(
            button_names[3], root), width=45)
        invs_button.pack()
    
    def to_sql(self, entries, text_box_names, category):
        """
        Sends all the user input to a monthly table in a SQL database
        
        Args:
        self ( _obj_ ) : Parent class object
        entries ( _obj_ ) : Text inputted by the user
        text_box_names ( _obj_ ) : Names of the text boxes
        category ( _obj_ ) : Transaction category
        
        Returns:
        Does not return
        """
        # Creates an instance of the SqlTasks class
        sql_tasks = scr_sql_tasks.SqlTasks()
        # Adds the record to the sql database. Replaces whitespace with underscore and converts
        # all letters to lowercase.
        sql_tasks.add_record(category.replace(' ','_').lower(), entries, text_box_names)
        self.logger.info(f'{category} record sent to SQL server: {entries}, {text_box_names}')

