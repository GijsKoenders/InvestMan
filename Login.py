# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:23:10 2019

@author: u303699
"""

import database
import Messages

def Loginscreen ():
    "Shows login screen in GUI"
    
    root = Tk()

    # Create this method before you create the entry
    def return_entry(root):
        """Gets and prints the content of the entry"""
        username = entry_username.get()
        pw = entry_password.get ()
        loginback (username, pw, root)
        
        
    LabelUsername = Label (root, text = "Please enter username")
    LabelPassword = Label (root, text = "Please enter your password")
    entry_username = Entry (root) # An entry is the same as the user input, a field where the user can input something
    entry_password = Entry (root, show = "*")


    LabelUsername.grid (row = 0, sticky = W) # With the sticky argument it is possible to stick something to eitherside of the column 
    # West (W) means left allgined and East (E) means right alligned)
    LabelPassword.grid (row = 1, sticky = W) 
    entry_username.grid (row = 0, column = 1) 
    entry_password.grid (row = 1, column = 1) # By using rows and columns it is possible to position labels, entries and buttons

    # Adding a button to actually log in
    Loginbut = Button (root, text = "Go!", command = lambda: return_entry (root) )
    Loginbut.grid (row = 2, sticky = W)
    
    # Adding a checkbox to ask if users want to stay logged in
    check = Checkbutton (root, text = "Keep me logged in")
    check.grid (row = 2, column = 1) # columnspann is the with of the widget

    # Connect the entry with the return button
 
    
    root.mainloop ()
    
def loginback (username, pw, root):
    " Login function"
    
    dbconnect ()
    
   # Extracting the usernames from the database
    query = "SELECT username FROM investman_login "
    c.execute(query)
    u_result = c.fetchall() 
    username_result = [list(i) for i in u_result] # Make a list of lists
    username_list = [item for sublist in username_result for item in sublist] # Flatten list
        

    #Extracting the passwords from the database
    query = "SELECT passwordu FROM investman_login"
    c.execute(query)
    p_result = c.fetchall() 
    password_result = [list(i) for i in p_result] # Make a list of lists
    password_list = [item for sublist in password_result for item in sublist]  # flatten list
    
    pw = hashing (pw)  
    pw = pw.hexdigest()
    zipped = zip(username_list, password_list) # Make a zipped file of usernames and passwords
    
    combination = False
    
    for name, pas in zipped: # Check if inputs are in the zipped list of usernames and passwords
        user = name
        word = pas
        if username == user and pw == word:
            combination = True
            root.destroy ()
            Startpage (username) # If username and password are correct -> open the startpage
            break

            
    if combination == False: # Give following output when combination of username and password is correct
            MessageManualWarning ( "False login", "Username and/or password is incorrect")
