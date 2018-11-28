#https://www.devdungeon.com/content/gui-programming-python#further-reading
#https://medium.com/@elan_73479/python-tkinter-tutorial-2-making-a-very-simple-login-889295115981
#https://www.youtube.com/watch?v=eJRLftYo9A0&index=8&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk
#LIVEGRAPH DATA WITH BTC

"""CREATE INVESTMAN"""
#Initialize InvestMan

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk 
from tkinter import ttk

import urllib
import json

import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 14)
MEDIUM_FONT = ("Verdana", 12)
SMALL_FONT = ("Verdana", 8)

style.use("ggplot")

"""CREATE POPUP"""
#Title of the popup



"""MAIN MENU"""

f = Figure()
a = f.add_subplot(111)

"""DEFINITIONS"""  


def popupmsg(msg):
    popup = tk.TK()
    
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=MEDIUM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destoy)
    B1.pacl()
    popup.mainloop
    
    
            


"""Frames"""

class root(tk.Tk):
        
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "InvestMan")
        
        container = tk.Frame(self)
        container.pack()
        
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        Crypto = tk.Menu(menubar, tearoff=0)
        Crypto.add_command(label="Bitcoin")
        Crypto.add_command(label="Ripple")
        Crypto.add_command(label="Ethereum")
        
        tk.Tk.config(self, menu=menubar)
        
        self.frames = {}
        for F in (StartPage, PageOne, BTCe_Page):        
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "ALPHA InvestMan")
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text= "Visit Page 1", command=lambda:controller.show_frame(PageOne))
        button1.pack()
        
        button = ttk.Button(self, text= "Visit Page 2", command=lambda:controller.show_frame(BTCe_Page))
        button.pack()
    
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Page One")
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text= "Visit Page 2", command=lambda:controller.show_frame(BTCe_Page))
        button1.pack()
        
        button1 = ttk.Button(self, text= "Back to Home", command=lambda:controller.show_frame(StartPage))
        button1.pack() 
        
        
class BTCe_Page(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Page Two")
        label.pack(pady=10, padx=10)
        
        button2 = ttk.Button(self, text= "Visit Page 1", command=lambda:controller.show_frame(PageOne))
        button2.pack()
        
        button2 = ttk.Button(self, text= "Back to Home", command=lambda:controller.show_frame(StartPage))
        button2.pack() 
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
        

app = root()
app.geometry("800x600")
ani = animation.FuncAnimation(f, interval=1000)
app.mainloop()



