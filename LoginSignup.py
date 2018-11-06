#https://www.devdungeon.com/content/gui-programming-python#further-reading
#https://medium.com/@elan_73479/python-tkinter-tutorial-2-making-a-very-simple-login-889295115981

"""CREATE INVESTMAN"""
#Initialize InvestMan
from tkinter import Tk, Menu, Label, Button, LEFT, Y, ttk, Entry
root = Tk()

"""CREATE POPUP"""
#Title of the popup
root.title("InvestMan")

#Grab the users' screenwidth and height for possible use
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("700x500+50+50")


"""MAIN MENU"""
#Create main menu bar
menu_bar = Menu(root)

# Create the submenu
file_menu = Menu(menu_bar, tearoff=0)
highscores_menu = Menu(menu_bar, tearoff=0)

# Add commands to submenu
file_menu.add_command(label="Login", command=root.destroy)
file_menu.add_command(label="Quit!", command=root.destroy)

# Add the "File" drop down sub-menu in the main menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Highscores", menu=highscores_menu)

"""DEFINITONS"""


def login(us1,pw1,usr,pword):
    if us1 == usr and pw1==pword:
       i=Label(gui,text='Login success').grid(row=6,column=0)
       print("login success")
    else:
       print("wrong password")
       j=Label(gui,text='Login failed').grid(row=6,column=0)

"""LOGINPAGE"""
#Text for LoginMenu
gui = Tk()
Entry(gui)

a = Label(gui ,text="username").grid(row=0,column = 0)
b = Label(gui ,text="password").grid(row=1,column=0)
e = Entry(gui).grid(row=0,column=1)
f = Entry(gui,show="*").grid(row=1,column=1)
c = Button(gui, text="Create account").grid(row=2,column=0)

a1 = Label(gui ,text="username").grid(row=3,column = 0)
b1 = Label(gui ,text="password").grid(row=4,column=0)
e1 = Entry(gui).grid(row=3,column=1)
f1 = Entry(gui,show="*").grid(row=4,column=1)

c1 = Button(gui, text="LOGIN",command=lambda : login(e,f,e1,f1)).grid(row=5,column=1)


root.config(menu=menu_bar)
gui.mainloop()
root.mainloop()
