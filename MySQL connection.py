
# coding: utf-8

# In[4]:


import MySQLdb as SQL


# In[15]:


conn = SQL.connect ("localhost", "root", db ="Investman db") # Defining connection to database
c = conn.cursor ()
c.execute ("INSERT INTO Accounts_and_pw (username, password) VALUES (username_input, password_input)")


# In[34]:


conn = SQL.connect ("localhost", "root", password = "Ballsdeep$22", db ="login_investman") # Defining connection to database"


# In[38]:


c = conn.cursor ()


# In[66]:


c.execute ("INSERT INTO accounts (username, password) VALUES ('Selimp20','selim298');")


# In[67]:


print(c.execute ("SELECT * FROM accounts"))


# In[70]:


print(c.execute ("SELECT * FROM accounts"))


# In[68]:


c.execute ("INSERT INTO accounts VALUES ('SELIM22','selim23');")


# In[71]:


c.execute ("SHOW TABLES")

