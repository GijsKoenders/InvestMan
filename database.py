# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:57:00 2019

@author: u303699
"""

def dbconnect():
    
    import MySQLdb as SQL # Import SQL package
    
    # Define connection to MySql database
    global conn
    conn = SQL.connect ("sql7.freemysqlhosting.net", "sql7273333",password = "mnInPtemi4", db ="sql7273333") 
    # Define cursor to be able to communicate to database
    global c
    c = conn.cursor ()
    
    
def hashing (pw): # Defining a function for hashing the passwords 
    import hashlib
    pw = pw.encode ('utf-8')
    hash1 = hashlib.md5 (pw)
    return hash1

Startframe ()