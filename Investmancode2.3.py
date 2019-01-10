# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# This is the first page what is seen when the application is first started

# First a couple of packages have to be installed

from tkinter import *
import MySQLdb as SQL # http://www.phpmyadmin.co/ -> Online database server
import hashlib
from PIL import ImageTk,Image


def Startframe ():
    
    Base = Tk ()

    Base.geometry ("600x800")
    textobject = Label (Base, text = "This is the Investman GUI", font = "Helvetica") # Creating a text object
    textobject.pack (side = LEFT)

    Startframe = Frame (Base, width = 300, height = 200) # Create start frame
    Startframe.pack (side = TOP) # Please it in the top corner and tell where to place it


    Signupbutton = Button (Startframe, text = "No account yet? Sign up here!", fg = "blue", command = signupscreen) # Creating buttons
    Loginbutton = Button (Startframe, text = "Sign in please!", fg = "green", command = Loginscreen) # fg = font colour, bg = background colour
    Quitbutton = Button (Startframe, text = "Get out of here!", fg = "red")

    Signupbutton.pack (side = RIGHT)
    Loginbutton.pack (side = RIGHT)
    Quitbutton.pack ()

    Base.mainloop ()
    
def hashing (pw): # Defining a function for hashing the passwords 
    pw = pw.encode ('utf-8')
    hash1 = hashlib.md5 (pw)
    return hash1
    
def signupscreen ():
    "Setting up the signup screen"
    
    base = Tk()
    

    # Create this method before you create the entry
    def return_entry():
        """Gets and prints the content of the entry"""
        username = entry_username.get()
        pw = entry_password.get ()
        signupback (username, pw)
        
    base.geometry ("200x300")    
    Message = Label (base, text = """We would like to welcome you into the world of Investman.
                                     Before we start you will be needing a username and a password.
                                     See you in a bit! """, fg = "green")
    Message.config (font = ("Verdana", 16)) # Configure font type
    
    LabelUsername = Label (base, text = "Enter the username of your choosing")
    LabelPassword = Label (base, text = "Please fill in your password")
    entry_username = Entry (base) # An entry is the same as the user input, a field where the user can input something
    entry_password = Entry (base, show = "*") 
    
    Message.grid (row = 1, sticky = W) # Place the welcome message into the grid
    
    LabelUsername.grid (row = 4, sticky = W) # With the sticky argument it is possible to stick something to eitherside of the column 
    # West (W) means left allgined and East (E) means right alligned)
    LabelPassword.grid (row = 6, sticky= W) 
    entry_username.grid (row = 4, column = 1, sticky = W) 
    entry_password.grid (row = 6, column = 1, sticky = W) # By using rows and columns it is possible to position labels, entries and buttons

    # Adding a button to confirm data
    Confirmbut = Button (base, text = "Confirm", command = return_entry)
    Confirmbut.grid (row = 7, columnspan = 2, sticky = W)

    # Connect the entry with the return button
 
    
    base.mainloop ()
    
def Loginscreen ():
    "Shows login screen in GUI"
    
    base = Tk()

    # Create this method before you create the entry
    def return_entry():
        """Gets and prints the content of the entry"""
        username = entry_username.get()
        pw = entry_password.get ()
        loginback (username, pw)
        
        
    LabelUsername = Label (base, text = "Please enter username")
    LabelPassword = Label (base, text = "Please enter your password")
    entry_username = Entry (base) # An entry is the same as the user input, a field where the user can input something
    entry_password = Entry (base, show = "*")


    LabelUsername.grid (row = 0, sticky = W) # With the sticky argument it is possible to stick something to eitherside of the column 
    # West (W) means left allgined and East (E) means right alligned)
    LabelPassword.grid (row = 1, sticky = W) 
    entry_username.grid (row = 0, column = 1) 
    entry_password.grid (row = 1, column = 1) # By using rows and columns it is possible to position labels, entries and buttons

    # Adding a button to actually log in
    Loginbut = Button (base, text = "Go!", command = return_entry)
    Loginbut.grid (row = 2, sticky = W)
    
    # Adding a checkbox to ask if users want to stay logged in
    check = Checkbutton (base, text = "Keep me logged in")
    check.grid (row = 2, column = 1) # columnspann is the with of the widget

    # Connect the entry with the return button
 
    
    base.mainloop ()

def signupback (username, pw):
    "Signing up to Investman"
    
    # Define connection to MySql database
    conn = SQL.connect ("sql7.freemysqlhosting.net", "sql7273333",password = "mnInPtemi4", db ="sql7273333") 
    # Define cursor to be able to communicate to database
    c = conn.cursor ()

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
                
            else:
                pw = hashing (pw)  
                pw = pw.hexdigest()
                user_pass = (username, pw)

            # Execute SQL command by passing in the string and the user variables (username and password)
            c.execute (my_string, user_pass)

            #Complete actions
            conn.commit ()
            conn.close ()
            Loginscreen ()
        
        except:
            MessageManualWarning ("Error", "We have entouraged an error, you possibly used an username that is already in use")
            continue
        break
    
    
def loginback (username, pw):
    " Login function"
    
    import MySQLdb as SQL # Import SQL package
    
    # Define connection to MySql database
    conn = SQL.connect ("sql7.freemysqlhosting.net", "sql7273333",password = "mnInPtemi4", db ="sql7273333") 
    # Define cursor to be able to communicate to database
    c = conn.cursor ()
    
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
            Startpage (username) # If username and password are correct -> open the startpage
            break

            
    if combination == False: # Give following output when combination of username and password is correct
            MessageManualWarning ( "False login", "Username and/or password is incorrect")
            
def Startpage (username):
    "Layout startpage"
    
    blankpage = Tk()
    
    
    # Initialize interface features
    blankpage.geometry ("600x800")
    Dropdown (root = blankpage)
    Toolbar (root = blankpage)
    Statusbar (root = blankpage)
    
    
    
    # Page content
    # Assign variables
    # img = PhotoImage(file = r"C:\Users\Selim Berntsen\Documents\Premaster_DSBG_CSAI\Basic Programming\Group assignment\50moneyphone.png")  
    # Does not work yet:
    # welcomepic = PhotoImage (file = 'C:/Users/Selim Berntsen/Documents/Premaster_DSBG_CSAI/Basic Programming/Group assignment/money.png')
    
    # Make content
    WelcomeMessage = Label (blankpage, text = "Welcome " + username + "! Ready to InvestMan?")
    WelcomeMessage.pack (side = TOP)
    WelcomeMessage.config (font = ("Verdana", 16)) # Configure font type
    # imgLabel = Label (blankpage, image = img)
    # imgLabel.pack (side = BOTTOM)
    blankpage.mainloop ()
    
def Accountdetails ():
    "Shows Account details in GUI"
    
    # Ofcource the dropdownmenu should be included as well, maybe as a class or maybe just as a function
    base = Tk()
    
    # Initialize interface features
    Dropdown (root = base) 
    Toolbar (root = base)
    Statusbar (root = base)

    # Page content
    Contentframe = Frame (base)
    Contentframe.pack (side = TOP)
    LabelUsername = Label (Contentframe, text = "username")
    LabelPassword = Label (Contentframe, text = "password")
    Username = Label (Contentframe, text = username)
    Password =Label(Contentframe, text = "xxxxxx")
    changepw = Button(Contentframe, text = "Change my password", fg = "red")
    
    LabelUsername.grid (row = 0, sticky = W) # With the sticky argument it is possible to stick something to eitherside of the column 
    # West (W) means left allgined and East (E) means right alligned)
    LabelPassword.grid (row = 1, sticky = W) 
    Username.grid (row = 0, column = 2) 
    Password.grid (row = 1, column = 2) # By using rows and columns it is possible to position labels, entries and buttons

    # Adding a checkbox to ask if users want to stay logged in

    changepw.grid (row = 2, columnspan = 3) # columnspann is the with of the widget

    base.mainloop ()
    
def Dropdown (root):
    "Creating a single dropdown menu for Investman"
    
    menu = Menu (root) # Menu function activation
    root.config (menu = menu) # Prepare our menu
    
    subMenu = Menu (menu) # Menu in a menu
    menu.add_cascade (label = "My account", menu = subMenu) # Obviously the label stands for the label of the menu, and the menu
    # argument creates a new dropdown
    subMenu.add_command (label = "Account details", command = Accountdetails)
    subMenu.add_separator ()
    
    # Adding another dropdown menu
    subMenu2 = Menu (menu)
    menu.add_cascade (label = "Portfolio", menu = subMenu2)
    subMenu2.add_command (label = "Crypto", command = print ("Crypto currency"))
    subMenu2.add_command (label = "Stocks", command = print ("Stocks"))
    
def Toolbar (root):
    "Creating a toolbar"
    toolbar = Frame (root)
    Logoutbut = Button (toolbar, text = "Log out", bg = "red", fg= "white", command = MessageboxAuto)
    Logoutbut.pack (side = RIGHT, padx = 4, pady = 3) # Displaying our button on the screen, by using padx and pady it is possible to leave space between
  # elements
    Ledgerbut = Button (toolbar, text = "Ledger", bg = "blue", fg= "white")
    Ledgerbut.pack (side = RIGHT, padx = 4, pady = 3)
    # Importing the canvas
    Canvasbut = Button (toolbar, text = "Graphics", bg = "green", fg= "white", command =InvestCanvas)
    Canvasbut.pack (side = RIGHT, padx = 4, pady = 3)
    
    toolbar.pack (side = TOP, fill = X)
    
def Statusbar (root):
    "Creation of the statusbar in the bottom of the window"
    
    status = Label (root, text = "Property of Selim Berntsen", bd = 1, relief = SUNKEN, anchor = W)
    status.pack (side= BOTTOM, fill = X)

def MessageboxAuto ():
    import tkinter.messagebox
    
    answer = tkinter.messagebox.askquestion ('Log out','Are you sure you want to log out?') # This question always generates a yes and a now answer
    
    # if answer == 'yes':
    #    root.quit  # Not able to get this part working
    
def MessageManualWarning (name, message):
    
    # Manually create a message box that solves your own problem
    import tkinter.messagebox as msg
    msg.showwarning (name, message)
    
def InvestCanvas ():
    
    root = Tk()
    mycanvas = Canvas (root, width = 600, height = 600)
    mycanvas.pack ()
    
    blueline = mycanvas.create_line (0, 0, 100, 400, fill = "blue") # First two arguments are your starting point, last two will be the ending point coordinates
    redline = mycanvas.create_line (50,50, 0, 500, fill = "red")
    Greenrectangle = mycanvas.create_rectangle (100,100, 200, 150, fill = "green") # First two arguments are the starting point of the rectangle,
    # the next two are the width and the height
    
    # mycanvas.remove (Greenrectangle) # Could use this method to remove certain elements in the canvas by using buttons or if
    # statement
    
    root.mainloop()
    
Startframe ()
            
            
            

            
            