
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Thu Nov 7 16:22:20 2018

@author: Selim Berntsen
@ Connection to online database
"""
# Import library for connecting to database

def signup ():
    "Signing up to Investman"
    
    
    import MySQLdb as SQL # Import SQL package

    # Write a SQL command and store it as a string. In this command we ask to store the username and the password in the database
    my_string = "INSERT INTO investman_login (username, passwordu, balance)" "VALUES (%s, %s, 100000)" # The user will get 100000 EU assigned to there account

    # Ask user to input username and password 

    while True: # This while loop is used to run the loop as long as the code gives no error
        try:
            username = input ()
        
            from string import punctuation, digits

            digitpw = False
            lowercase = False
            uppercase = False

            while digitpw == False or lowercase == False or uppercase == False:
                password = input()
                for char in password:
                    if char in digits:
                        digitpw = True
                    elif char.islower():
                        lowercase = True
                    elif char.isupper():
                        uppercase = True
                    elif char == " ":
                        break
                    
        
            user_pass = (username, password)
        
            # Define connection to MySql database
            conn = SQL.connect ("sql7.freemysqlhosting.net", "sql7262826",password = "lGkGuxIww8", db ="sql7262826") 

            # Define cursor to be able to communicate to database
            c = conn.cursor ()

            # Execute SQL command by passing in the string and the user variables (username and password)
            c.execute (my_string, user_pass)

            #Complete actions
            conn.commit ()
            conn.close ()

    
        except:
            continue
        break
   
       




# In[4]:


signup()

