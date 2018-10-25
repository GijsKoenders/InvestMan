# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:22:20 2018

@author: Selim Berntsen
@ Connection to online database
"""

string = "INSERT INTO investman_login (username, passwordu, balance)" "VALUES (%s, %s, 100000)"
username = input ()
password = input ()
user_pass = (username, password)


conn = SQL.connect ("sql7.freemysqlhosting.net", "sql7262826",password = "lGkGuxIww8", db ="sql7262826") # Defining connection to database
c = conn.cursor ()
c.execute (string, user_pass)
conn.commit ()
conn.close ()

