# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:38:02 2019

@author: u303699
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# This is the first page what is seen when the application is first started

# First a couple of packages have to be installed

from tkinter import *
#import MySQLdb as SQL # http://www.phpmyadmin.co/ -> Online database server
from PIL import ImageTk,Image
import Messages
import Signup
import Login
import Init

def Startframe ():
    
    root = Tk ()

    root.geometry ("600x800")
    textobject = Label (root, text = "This is the Investman GUI", font = "Helvetica") # Creating a text object
    textobject.pack (side = LEFT)

    Startframe = Frame (root, width = 300, height = 200) # Create start frame
    Startframe.pack (side = TOP) # Please it in the top corner and tell where to place it


    Signupbutton = Button (Startframe, text = "No account yet? Sign up here!", fg = "blue", command = signupscreen) # Creating buttons
    Loginbutton = Button (Startframe, text = "Sign in please!", fg = "green", command = Loginscreen) # fg = font colour, bg = background colour
    Quitbutton = Button (Startframe, text = "Get out of here!", fg = "red", command = root.destroy)

    Signupbutton.pack (side = RIGHT)
    Loginbutton.pack (side = RIGHT)
    Quitbutton.pack ()

    root.mainloop ()

            
def Startpage (username):
    "Layout startpage"
    
    root = Tk()
    
    
    init (root, username)
    
    # Page content
    # Assign variables
    # img = PhotoImage(file = r"C:\Users\Selim Berntsen\Documents\Premaster_DSBG_CSAI\Basic Programming\Group assignment\50moneyphone.png")  
    # Does not work yet:
    # welcomepic = PhotoImage (file = 'C:/Users/Selim Berntsen/Documents/Premaster_DSBG_CSAI/Basic Programming/Group assignment/money.png')
    
    # Make content
    WelcomeMessage = Label (root, text = "Welcome " + username + "! Ready to InvestMan?")
    WelcomeMessage.pack (side = TOP)
    WelcomeMessage.config (font = ("Verdana", 16)) # Configure font type
    # imgLabel = Label (root, image = img)
    # imgLabel.pack (side = BOTTOM)
    root.mainloop ()
    
def Accountdetails (username):
    "Shows Account details in GUI"
    
    # Ofcource the dropdownmenu should be included as well, maybe as a class or maybe just as a function
    root = Tk()
    
    init (root, username)
    
#     # Initialize interface features
#     Dropdown (root, username) 
#     Toolbar (root)
#     Statusbar (root)

    # Page content
    Contentframe = Frame (root)
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

    root.mainloop ()
    
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
 
    


    

    

            

            
            

            
            

