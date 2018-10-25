# -*- coding: utf-8 -*-+-*
"""
Investman
"""

print ("Welcome to InvestMan! The best and most epic investment game made by premaster students")
print ("Press enter to start playing the game") # Welcomewords


continue1 = input () 

if continue1 == "": # Check if user only entered the enter shift
    login1 = input ("If you already have a username choose 1, if you want to login with a existing username just type enter")
    if login1 == "1":
        print ("Hey there investor! So you are investing for the first time. Well since you are new in this thing, you will be coming here a lot")
        print ("For this purpose it is convenient to make your own login so we can store your money savely")
        
        import MySQLdb as SQL # For the purpose of saving usernames and passwords we will need a database to connect it to
        # conn = SQL.connect ("localhost", "Selim Berntsen", db ="Investman db" # Defining connection to database
        # c = conn.cursor ()
        # c.execute ("INSERT INTO Accounts_and_pw (username, password) VALUES (username_input, password_input)")
        # rows = c.fetchall()
        # for eachrow in rows:
        #    print (eachrow
        # This code imports data from a table into python
        
        username_input = input ("Please enter your desired username below\n") # The user chooses his username
        password_input = input ("Please choose a safe password\n") # The user chooses his password
    
    # 
        
    
else:
    break

