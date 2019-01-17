# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:28:04 2019

@author: gijsd
"""

import tkinter as tk
#import MySQLdb as SQL # http://www.phpmyadmin.co/ -> Online database server
import Messages
import webscraper as ws
import database
import Runner

def init (root, username, geo = "500x400"):
    "Initialize frame and standard features"
    root.geometry (geo)
    Dropdown (root, username) 
    Toolbar (root, username)
    Statusbar (root)

def Dropdown (root, username):
    "Creating a single dropdown menu for Investman"
    
    # Creating a menu and activating function possiblities
    menu = tk.Menu (root)
    root.config (menu = menu)
    
    # Argument creating multiple menus in the menubar
    subMenu = tk.Menu (menu)
    menu.add_cascade (label = "Settings", menu = subMenu) # Obviously the label stands for the label of the menu, and the menu
    subMenu.add_command (label = "Account details", command = lambda: Accountdetails (username))
    subMenu.add_command (label = "Disclaimer", command = lambda: Disclaimer())
    subMenu.add_command (label = "Logout", command = lambda: Messages.MessageboxAuto (root))
    subMenu.add_command (label = "Exit", command = root.destroy)
    
    subMenu2 = tk.Menu (menu)
    menu.add_cascade (label = "Cryptocurrency", menu = subMenu2)
    subMenu2.add_command (label = "Investing overview", command = lambda: Invest (username))
    subMenu2.add_command (label = "Bitcoin", command = lambda: cryptowindow (username, bitbalance, "Bitcoin", root))
    subMenu2.add_command (label = "Ethereum", command = lambda: cryptowindow (username, ethbalance, "Ethereum", root))
    subMenu2.add_command (label = "Substratum", command = lambda: cryptowindow (username, subsbalance, "Substratum", root))
    subMenu2.add_command (label = "Ripple", command = lambda: cryptowindow (username, ripbalance, "Ripple", root))
    
    subMenu3 = tk.Menu (menu)
    menu.add_cascade (label = "Highscores", menu = subMenu3)
    
# We wanted to add an easy access menu toolbar at the bottom, plus, it looks good :)    
def Toolbar (root, username):
    "Creating a toolbar"
    
    toolbar = tk.Frame (root)
    
    #Creating three easy access buttons on the bottom of the page
    Investbut = tk.Button (toolbar, text = "Invest!", bg = "green", fg= "white", command = lambda: Invest (username))
    Investbut.pack (side = "left", padx = 4, pady = 3) # Displaying our button on the screen, by using padx and pady it is possible to leave space between
    
    Ledgerbut = tk.Button (toolbar, text = "Highscores", bg = "blue", fg= "white")
    Ledgerbut.pack (side = "left", padx = 4, pady = 3)
    
    Graphbut = tk.Button (toolbar, text = "Charts", bg = "Purple", fg= "white", command = Runner.Runapp)
    Graphbut.pack (side = "left", padx = 4, pady = 3)
    
    Logoutbut = tk.Button (toolbar, text = "Log out", bg = "red", fg= "white", command = lambda: Messages.MessageboxAuto (root)) 
    Logoutbut.pack (side = "left", padx = 4, pady = 3) 
   
    toolbar.pack (side = "top", fill = "x")
    
def Statusbar (root):
    "Creation of the statusbar in the bottom of the window"
    status = tk.Label (root, text = "Property of Selim Berntsen, Julian van Bree and Gijs Koenders", bd = 1, relief = "sunken", anchor = "w")
    status.pack (side = "bottom", fill = "x")


def Startframe ():
    
    root = tk.Tk ()
    root.title("Investman")
    root.geometry ("450x200")
    
    textobject = tk.Label(root, text = "Welcome to Investman!", font='Verdana 18 bold') # Creating a text object
    textobject.pack ()
    
    textobject1 = tk.Label(root, text = """
    Investman is a small game created for the Basic Programming course at
    Tilburg University. In Investman you can invest in cryptocurrency updated 
    in real-time and try to beat your friends by investing wisely and beating 
    \tthem in the highscores! Thank you for playing our game!                     
    """)
    textobject1.pack ()
    
    textobject2 = tk.Label(root, text = "Please select one of the following options to continue :\n") # Creating a text object
    textobject2.pack ()

    Startframe = tk.Frame (root, width = 300, height = 200) # Create start frame
    Startframe.pack (side = "top") # Please it in the top corner and tell where to place it

    Signupbutton = tk.Button (Startframe, text = "No account yet? Sign up here!", fg = "blue", command = signupscreen) # Creating buttons
    Loginbutton = tk.Button (Startframe, text = "Sign me in!", fg = "green", command = Loginscreen) # fg = font colour, bg = background colour
    Quitbutton = tk.Button (Startframe, text = "Get me out of here!", fg = "red", command = root.destroy)

    Quitbutton.pack (side = "right")
    Signupbutton.pack (side = "right")
    Loginbutton.pack (side = "right")
    
    root.mainloop ()


def Startpage (username):
    "Layout startpage"
    
    root = tk.Tk()
    root.title ("Investman")
    root.geometry ("600x600")
    init (root, username)
    
    #img = PIL.Image.open("moneyphone.jpg") 
    # Does not work yet:
    
    Titlemessage = tk.Label (root, text = "Welcome " + username + """ once again to Investman!
    Are you ready to InvestMan??.\n""", font = "Verdana 14 bold")
    Titlemessage.pack ()
    #imgLabel = tk.Label (root, image = img)
    #imgLabel.pack (side = BOTTOM, expand = "yes")
    root.mainloop ()
    
    
def Disclaimer ():
    
    root = tk.Tk ()
    root.title("Disclaimer")
    root.geometry ("650x300")
    
    textobject = tk.Label(root, text = "The man that invests", font='Verdana 18 bold')
    textobject.pack()
    
    textobject1 = tk.Label(root, text = "InvestMan is the game in which man invests", font='Verdana 12 bold')
    textobject1.pack()
    
    textobject2 = tk.Label(root, text = """
    *The InvestMan brand is intellectual property of Gijs Koenders, Julian van Bree, and Selim Berntsen. 
    *The Lawyers of the InvestMan brand pointed out to disclaim the following: 
    *The InvestMan brand does not exclude any religious, gender, or other potential minority groups 
    that may be harmed by the intellectual property. 
    *The 'Man' in the InvestMan brand might be misleading, as the 'Man' stands for Metropolitan Area Network (MAN). 
    *This means that the full name of the InvestMan brand is: 'Invest Metropolitan Area Network brand. 
    *The subtitle: The man that invests = The Metropolitan Area Network that invests. 
    *The description: InvestMan is the game in which man invests = Invest Metropolitan 
    Area Network is the game in which Metropolitan Area Network invests                    
    """)
    textobject2.pack()

    Quitbutton = tk.Button (root, text = "This does not make any sense!", command = root.destroy)
    Quitbutton.pack()
    
    root.mainloop ()
    

def Accountdetails (username):
    "Shows Account details in GUI"
    
    # Ofcource the dropdownmenu should be included as well, maybe as a class or maybe just as a function
    root = tk.Tk()
    
    init (root, username)
    data = getdbvalues ()
    
    
#     # Initialize interface features
#     Dropdown (root, username) 
#     Toolbar (root)
#     Statusbar (root)

    # Page content
    Contentframe = tk.Frame (root)
    Contentframe.pack (side = "top")
    LabelUsername = tk.Label (Contentframe, text = "username")
    LabelPassword = tk.Label (Contentframe, text = "password")
    Username = tk.Label (Contentframe, text = username)
    Password =tk.Label(Contentframe, text = "xxxxxx")
    changepw = tk.Button(Contentframe, text = "Change my password", fg = "red")
    LabelBalance = tk.Label (Contentframe, text = "Your balance ")
    BalanceAmount = tk.Label (Contentframe, text = "$" + "100")
    
    LabelUsername.grid (row = 0, sticky = "w") # With the sticky argument it is possible to stick something to eitherside of the column 
    # West (W) means left allgined and East (E) means right alligned)
    LabelPassword.grid (row = 1, sticky = "w")
    LabelBalance.grid (row = 2, sticky = "w")
    Username.grid (row = 0, column = 2) 
    Password.grid (row = 1, column = 2) # By using rows and columns it is possible to position labels, entries and buttons
    BalanceAmount.grid  (row = 2, column = 2)   
    changepw.grid (row = 3, columnspan = 3) # columnspann is the with of the widget

    root.mainloop ()
    


def signupscreen ():
    "Setting up the signup screen"
    
    root = tk.Tk()
    root.title("SignUp")
    root.geometry ("450x200")   

    # Create this method before you create the entry
    def return_entry(root):
        """Gets and prints the content of the entry"""
        username = entry_username.get()
        pw = entry_password.get ()
        signupback (username, pw, root)
    
    # Create all messages and entries needed on the page
    Message = tk.Label (root, text = """Welcome once again to Investman!
    Please follow the instructions below to create your account.\n""", font='Verdana 10')
    LabelUsername = tk.Label (root, text = "Pick your preferred username:")
    LabelPassword = tk.Label (root, text = "Pick your preferred password:")
    entry_username = tk.Entry (root) # An entry is the same as the user input, a field where the user can input something
    entry_password = tk.Entry (root, show = "*") 
    InfoLabel = tk.Label (root, text = """Attention! 
    Your password needs at least one lowercase, one uppercase and one number!""", fg = "red")
    
    # Place all the messages in a grid, by using rows and columns it is possible to position labels, entries and buttons
    Message.grid (row = 1, columnspan = 4, sticky = "w")
    LabelUsername.grid (row = 4, sticky = "w")
    LabelPassword.grid (row = 6, sticky= "w") 
    entry_username.grid (row = 4, column = 1, sticky = "w") 
    entry_password.grid (row = 6, column = 1, sticky = "w") 
    InfoLabel.grid (row = 8, columnspan = 4, sticky = "w")
    
    # Adding a button to confirm data
    Confirmbut = Button (root, text = "Confirm", command = lambda: return_entry (root))
    Confirmbut.grid (row = 7, columnspan = 2, sticky = "e")

    root.mainloop ()


def signupback (username, pw, root):
    "Signing up to Investman"
    
    conn, c = dbconnect () # Connect to online database

    # Write a SQL command and store it as a string. In this command we ask to store the username and the password in the database
    my_string = "INSERT INTO investman_login (username, password, balance)" "VALUES (%s, %s, 100000)" # The user will get 100000 EU assigned to there account

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
        
        except Exception as error:
            print ("error " + repr(error))
            MessageManualWarning ("Error", "We have entouraged an error, you possibly used an username that is already in use")
            break
        break
    
def Loginscreen ():
    "Shows login screen in GUI"
    
    root = tk.Tk()

    root.title("Login")
    root.geometry ("300x100")

    # Create this method before you create the entry
    def return_entry(root):
        """Gets and prints the content of the entry"""
        username = entry_username.get()
        pw = entry_password.get ()
        loginback (username, pw, root)
        
    # Create all messages and entries needed on the page    
    Message = tk.Label (root, text = "Please enter your login details below", font='Verdana 10')
    LabelUsername = tk.Label (root, text = "Please enter username")
    LabelPassword = tk.Label (root, text = "Please enter your password")
    entry_username = tk.Entry (root) # An entry is the same as the user input, a field where the user can input something
    entry_password = tk.Entry (root, show = "*")

    # Place all the messages in a grid, by using rows and columns it is possible to position labels, entries and buttons
    Message.grid (row = 0, columnspan = 4, sticky = "w")
    LabelUsername.grid (row = 1, sticky = "w")
    LabelPassword.grid (row = 2, sticky = "w") 
    entry_username.grid (row = 1, column = 1) 
    entry_password.grid (row = 2, column = 1)

    # Adding a button to actually log in
    Loginbut = tk.Button (root, text = "Log me in!", command = lambda: return_entry (root) )
    Loginbut.grid (row = 3, sticky = "w")
 
    
    root.mainloop ()
    
def loginback (username, pw, root):
    " Login function"
    
    conn, c = dbconnect ()
    
   # Extracting the usernames from the database
    query = "SELECT username FROM investman_login "
    c.execute(query)
    u_result = c.fetchall() 
    username_result = [list(i) for i in u_result] # Make a list of lists
    username_list = [item for sublist in username_result for item in sublist] # Flatten list
        

    #Extracting the passwords from the database
    query = "SELECT password FROM investman_login"
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
            
def Invest (username):
        
    root = tk.Tk ()
    
    #getdbvalues (username) # Importing values into the page still has to happen
    
    data = getdbvalues (username) # Retrieving the user data (balance information)
    
    balance = data [0]
    bitbalance = data [1]
    ripbalance = data [2]
    ethbalance = data [3]
    subsbalance = data [4]
    
    balance = round(balance, 2)
    
    prices = ws.prices()
    bitcoin_price = round(float(prices[0]),4)
    ethereum_price = round(float(prices[1]), 4) 
    ripple_price = round(float(prices[2]), 4)
    substratum_price = round(float(prices[3]), 4)
    
    profits = ((balance - 100000)/100000) * 100    
    profits = str(profits)
    
    
    # print (balance)

    text1 = tk.Label (root, text = "So you think you are ready to invest?", font = "Verdana") # Creating a text object
    # Maybe include a show me what you got image
    text2 = tk.Label (root, text = "Choose from the panel where you want to invest in", font = "Verdana")
    balancewindow = tk.Label (root, text = "Your balance is $"  ,font = "Verdana")
    amountwindow = tk.Label (root, text = balance ,font = "Verdana 14 bold")
    # How to put balance in text parameter + str(balance)
    profitswindow = tk.Label (root, text = "Profits: " + profits + "%" ,font = "Verdana")
    BackBut = tk.Button (root, text = "Go back to startpage", bg = "orange", fg= "white", command = lambda: Startpage (username))
    
    def choosebut (name, col, com, rown, coln):
        button = tk.Button (root, text = name, bg = col, fg = "white", command = com)
        button.grid(row = rown, column = coln)    
        
    choosebut ("Bitcoin", "blue", lambda: cryptowindow (username, bitbalance, 
                                                        bitcoin_price, "Bitcoin"), 6, 1)
    choosebut ("Ripple", "red", lambda: cryptowindow (username, ripbalance,
                                                      ripple_price, "Ripple"), 6, 2)
    choosebut ("Ethereum", "green", lambda: cryptowindow (username, ethbalance,
                                                          ethereum_price, "Ethereum"), 7, 1)
    choosebut ("Substratum", "purple", lambda: cryptowindow (username, subsbalance,
                                                             substratum_price, "Substratum"), 7, 2)

    text1.grid (row =1, columnspan = 3)
    text2.grid (row = 5, columnspan = 3)
    balancewindow.grid (row = 3, columnspan = 2 )
    amountwindow.grid (row = 3, column= 2)
    profitswindow.grid (row = 4)
    BackBut.grid (row = 0, column = 9)
    
    
    root.mainloop ()
    
    return balance
    
def cryptowindow (username, bal, price, name):
    
    root = tk.Tk ()
    
    init (root, username) # Initializing
    
    # price = str(price)
    
    amount1 = tk.Label (root, text = "Your current balance in " + name + " is ", font = "Verdana") 
    amount2 = tk.Label (root, text = bal, font = "Verdana")
    
    price1 = tk.Label (root, text = "The current price of " + name + " in dollars is ", font = "Verdana") 
    price2 = tk.Label (root, text = price, font = "Verdana")
    
    tradebut = tk.Button (root, text = "Buy or sell " + name, font = "Arial", bg = "green",
                          command = lambda: Trade (username, bal, price, name)) # Soon to become trade window 
    
    amount1.pack (side = "top")
    amount2.pack (side = "top")
    price1.pack (side = "top")
    price2.pack (side = "top")
    tradebut.pack (side = "bottom")
    
    root.mainloop ()
    
def Trade (username, bal, price, name):
    "Window to buy and sell stocks"
    
    root = tk.Tk()
    
    def input_trade (choice):
        trade = float(TraderEntry.get ())
        Buyorsell (username, choice, bal, price, name, trade)
        
    # Page content
    Trader = tk.Label(root, text = "Amount that man invests in (either buy or sell " + name)
    TraderEntry = tk.Entry(root)
    BuyBut = tk.Button (root, text = "Buy " + name, command =  lambda: input_trade ("buy")) 
    SellBut = tk.Button (root, text = "Sell " + name, command = lambda: input_trade ("sell"))
    
    Trader.grid (row = 2, sticky = "w")
    TraderEntry.grid (row = 2, column = 2) 
    BuyBut.grid (row = 4, column = 1) # By using rows and columns it is possible to position labels, entries and buttons
    SellBut.grid  (row = 4, column = 2)   

    root.mainloop ()

def Buyorsell (username, choice, bal, price, name, trade):
    """Gets and prints the content of the entry"""
        
    balance = Invest (username) # Getting the balance variable
        
    # What if float is false?? 
    if choice == "buy":
        if trade > balance:
            MessageManualWarning ("Balance error", "Isufficient funds")
        else: 
            BuyBackend (username, bal, price, trade, name)
            MessageManualInfo ("Confirmation", "Your trade has been confirmed")
    else:
        if trade > bal:
            MessageManualWarning ("Balance error", "Isufficient funds")
        else:
            SellBackend (username, bal, price, trade, name)
            MessageManualInfo ("Confirmation", "Your trade has been confirmed")
            
    
def BuyBackend (username, bal, price, trade, name):
    "Calculations are made and sellinginformation gets exported to the database" 
    
    # Trade calculations
    balance = Invest (username)
    newbalance = balance - trade
    investment = trade / price
    newbal = bal + investment
    
    print (newbalance)
    print (newbal)
    
    # Communicate information to database
    database.insertdbvalues (username, newbalance, newbal, name)
    
    Invest (username) # Return to the invest page
    
def SellBackend (username, bal, price, trade, name):
    "Calculations are made and selling information gets exported to the database"
    
    # Trade calculations
    balance = Invest (username)
    newbalance = balance + trade
    investment = trade * price
    newbal = bal - investment
    
    # Communicate information to database
    database.insertdbvalues (username, newbalance, newbal, name)
    
    Invest (username) # Return to the investpage
    
Startframe ()
    
    

    

    
