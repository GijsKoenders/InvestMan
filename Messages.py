# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:52:43 2019

@author: u303699
"""

def MessageboxAuto (root):
    
    import tkinter.messagebox
    
    answer = tkinter.messagebox.askquestion ('Log out','Are you sure you want to log out?') # This question always generates a yes and a now answer
    
    if answer == 'yes':
        root.destroy () 
        
def MessageManualWarning (name, message):
    
    # Manually create a message box that solves your own problem
    import tkinter.messagebox as msg
    msg.showwarning (name, message)