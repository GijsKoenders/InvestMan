
# coding: utf-8

# In[5]:


def login ():
    " Login function"
    
    import MySQLdb as SQL
    
    # Define connection to MySql database
    conn = SQL.connect ("sql7.freemysqlhosting.net", "sql7262826",password = "lGkGuxIww8", db ="sql7262826") 

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
    
    combination = False # Flag variable
    
    while combination == False: 

        username = input ("Your username\n")
        pw = input ("Your password\n")
        pw = hashing (pw)  
        pw = pw.hexdigest()
        zipped = zip(username_list, password_list) # Make a zipped file of usernames and passwords
    
        for name, pas in zipped: # Check if inputs are in the zipped list of usernames and passwords
            user = name
            word = pas
            if username == user and pw == word:
                print("Welcome " + user)
                combination = True
            
        if combination == False: # Give following output when combination of username and password is correct
            print("Sorry, wrong combination of username and password. Try again")


# In[1]:


import hashlib

def hashing (pw):
    pw = pw.encode ('utf-8')
    hash1 = hashlib.md5 (pw)
    return hash1 


# In[ ]:


login()

