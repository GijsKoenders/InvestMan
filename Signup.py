# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:00:52 2019

@author: u303699
"""

import database
import Messages
from tkinter import *

def signupscreen ():
    "Setting up the signup screen"
    
    root = Tk()
    

    # Create this method before you create the entry
    def return_entry(root):
        """Gets and prints the content of the entry"""
        username = entry_username.get()
        pw = entry_password.get ()
        signupback (username, pw, root)
        
    root.geometry ("200x300")    
    Message = Label (root, text = """We would like to welcome you into the world of Investman.
                                     Before we start you will be needing a username and a password.
                                     See you in a bit! """, fg = "green")
    Message.config (font = ("Verdana", 16)) # Configure font type
    
    LabelUsername = Label (root, text = "Enter the username of your choosing")
    LabelPassword = Label (root, text = "Please fill in your password")
    entry_username = Entry (root) # An entry is the same as the user input, a field where the user can input something
    entry_password = Entry (root, show = "*") 
    
    Message.grid (row = 1, sticky = W) # Place the welcome message into the grid
    
    LabelUsername.grid (row = 4, sticky = W) # With the sticky argument it is possible to stick something to eitherside of the column 
    # West (W) means left allgined and East (E) means right alligned)
    LabelPassword.grid (row = 6, sticky= W) 
    entry_username.grid (row = 4, column = 1, sticky = W) 
    entry_password.grid (row = 6, column = 1, sticky = W) # By using rows and columns it is possible to position labels, entries and buttons

    # Adding a button to confirm data
    Confirmbut = Button (root, text = "Confirm", command = lambda: return_entry (root))
    Confirmbut.grid (row = 7, columnspan = 2, sticky = W)

    # Connect the entry with the return button
 
    
    root.mainloop ()


def signupback (username, pw, root):
    "Signing up to Investman"
    
    dbconnect () # Connect to online database

    # Write a SQL command and store it as a string. In this command we ask to store the username and the password in the database
    my_string = "INSERT INTO investman_login (username, passwordu, balance)" "VALUES (%s, %s, 100000)" # The user will get 100000 EU assigned to there account

    # Create username and password from entries
            
    while True: # This while loop is used to run the loop as long as the code gives no error
        try:    
    
            from string import punctuation, digits

            digitpw = False
            lowercase = False
            uppercase = False

            for char in pw:
                if char in digits:
                    digitpw = True
                elif char.islower():
                    lowercase = True
                elif char.isupper():
                    uppercase = True
                elif char == " ":
                    break
                    
            if digitpw == False or lowercase == False or uppercase == False:
                MessageManualWarning ("Error", "Your password does not meet the given requirements")
                break
                
            else:
                pw = hashing (pw)  
                pw = pw.hexdigest()
                user_pass = (username, pw)

            # Execute SQL command by passing in the string and the user variables (username and password)
            c.execute (my_string, user_pass)

            #Complete actions
            conn.commit ()
            conn.close ()
            root.destroy ()
            Loginscreen ()
        
        except:
            MessageManualWarning ("Error", "We have entouraged an error, you possibly used an username that is already in use")
            break
        break



