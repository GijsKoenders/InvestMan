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

matplotlib.use("TkAgg")
style.use("ggplot")

"""CREATE POPUP"""
#Title of the popup



"""MAIN MENU"""

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

"""DEFINITIONS"""
def animate(i):
    pullData = open("sampleData.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList)
            
            


"""Frames"""

class root(tk.Tk):
        
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.wm_title(self, "InvestMan")
        
        container = tk.Frame(self)
        container.pack()
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):        
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
        label = tk.Label(self, text= "Start Page")
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text= "Visit Page 1", command=lambda:controller.show_frame(PageOne))
        button.pack()
        
        button = ttk.Button(self, text= "Visit Page 2", command=lambda:controller.show_frame(PageTwo))
        button.pack()
    
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Page One")
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text= "Visit Page 2", command=lambda:controller.show_frame(PageTwo))
        button1.pack()
        
        button1 = ttk.Button(self, text= "Back to Home", command=lambda:controller.show_frame(StartPage))
        button1.pack() 
        
        
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text= "Page Two")
        label.pack(pady=10, padx=10)
        
        button2 = ttk.Button(self, text= "Visit Page 1", command=lambda:controller.show_frame(PageOne))
        button2.pack()
        
        button2 = ttk.Button(self, text= "Back to Home", command=lambda:controller.show_frame(StartPage))
        button2.pack() 
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
        

app = root()
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()



