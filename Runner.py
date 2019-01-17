# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:24:19 2018

@author: Gijs Koenders
"""

"""These are the modules used for the application, there remain to be some buggy functions, such as the\n
realtime price functions. These functions open in a window in which continues endlessly, not sure how to stop :("""

"""Import of modules used:"""

#Matplotlib is used for plotting charts 
#Tkinter is used for making application pages
#Requests is used to GET information from a web URL
#Lxml is used to READ the JSON files which are received with the requests module
#Time helps the realtime graph update
#Re is used to find strings matching the relevant coin criteria


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style 
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import tkinter as tk
from tkinter import ttk
import requests
from lxml import html
from time import sleep
import re

#Font used for headers
LARGE_FONT= ("Verdana", 12)

#Style of graphs
style.use("ggplot")

#Bitcoin OHLC information (OHLC = Open, High, Low, Close)
bitcoin_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/btcusd/ohlc")
bitcoin_ohlc_link = bitcoin_ohlc_link.text
bitcoin_ohlc_link = bitcoin_ohlc_link.split(",")
bitcoin_price = float(bitcoin_ohlc_link[-7])

#Ethereum OHLC information(OHLC = Open, High, Low, Close)
ethereum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/ethusd/ohlc")
ethereum_ohlc_link = ethereum_ohlc_link.text
ethereum_ohlc_link = ethereum_ohlc_link.split(",")

#Ripple OHLC information (OHLC = Open, High, Low, Close)
ripple_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/xrpbtc/ohlc")
ripple_ohlc_link = ripple_ohlc_link.text
ripple_ohlc_link = ripple_ohlc_link.split(",")

#Substratum OHLC information (ohlc = Open, High, Low, Close)
substratum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/subbtc/ohlc")
substratum_ohlc_link = substratum_ohlc_link.text
substratum_ohlc_link = substratum_ohlc_link.split(",")

def bitcoin():
    
    """This is the Bitcoin webscrapper
    Please note that the Bitcoin webscrapper is quite similar to the Ethereum, Ripple, and
    Substratum scrapper. For that reason, only this section has been commented. Understanding
    this function means that the other webscrapping functions will be understood correctly.
    """
    
    #Store information to make charts, figure is plotted
    bitcoin_historic = []
    bitcoin_list = []
    fig = plt.figure()
    
    #Make a loop to receive live price information (exchange = coinbase-pro)
    while True:  
        #Clear plot (or else the charts stack on top of each other)
        plt.clf()
        
        #JSON file that is scrapped, and how it generates only relevant information
        scrape = requests.get("https://api.cryptowat.ch/markets/prices")
        scrape_content = html.fromstring(scrape.content)
        scrape_link = scrape_content.xpath("text()")
        scrape_link = scrape_link[0]
    
        #Re module to find relevant information 
        bitcoin_ticker = re.findall(r'coinbase-pro:btc":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:btcusd":+\d+', scrape_link)  
        allowance = re.findall(r'remaining":+\d+', scrape_link)
        
        #Actual price of bitcoin as a string
        bitcoin_price = re.findall(r'\d+\.+\d+', bitcoin_ticker[0]) or re.findall(r'\d+', bitcoin_ticker[0])
        allowance = re.findall(r'\d+', allowance[0])
        
        #Actual price of Bitcoin converted into a loose element
        #Allowance determines how many calls to the JSON file can be made
        bitcoin_price = bitcoin_price[0]
        allowance = allowance[0]
        
        #Element converted into a float
        bitcoin_price = float(bitcoin_price)
        allowance = int(allowance)
        
        #Historic price information to plot a chart
        bitcoin_historic.append(bitcoin_price)
        
        #Look for unique values in the list
        bitcoin_historic_set = set(bitcoin_historic)
        
        #If statement that kicks in to decrease the chart ones it becomes too long, or dense
        if len(bitcoin_historic_set) == 10 or len(bitcoin_historic) >100:
            bitcoin_historic.pop(0)
        
        #Plotting the chart, giving appropriate labels
        axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
        axes1.set_title("Bitcoin Price")
        axes1.set_xlabel("Iterations")
        axes1.set_ylabel("In Dollars")
        
        #Gather information for displaying line 
        if bitcoin_historic[-1] not in bitcoin_list:
            bitcoin_list.append(bitcoin_historic[-1])
        
        #Determine colour of the line (blue = no action, green = upward action, red = downward action (hex-codes are used))
        if len(bitcoin_list) == 1:
            axes1.plot(bitcoin_historic,"#7f7fff")
        if len(bitcoin_list) >= 2:
            if bitcoin_list[-1] > bitcoin_list[-2]:
                axes1.plot(bitcoin_historic, color = "#00870b")
            elif bitcoin_list[-1] < bitcoin_list[-2]:
                axes1.plot(bitcoin_historic, color = "#ff0000")
        
        #Making sure that no scientific information is displayed (especially important for the coins costing less than one dollar)
        axes1.ticklabel_format(useOffset=False, style='plain')
        
        #Actually drawing the plot
        plt.draw()
        
        #8000000000 ms worth of CPU power can be retreived from the server,
        #once it hits certain thresholds, the updating time alters
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(17)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(7)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(2)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)
        #Plot pause 
        plt.pause(3)
   
    #return the function 
    return 

def ethereum():
    
    """This is the Ethereum webscrapper"""
    
    ethereum_historic = []
    ethereum_list = []
    fig = plt.figure()

    while True:
        fig.clf()
        scrape = requests.get("https://api.cryptowat.ch/markets/prices")
        scrape_content = html.fromstring(scrape.content)
        scrape_link = scrape_content.xpath("text()")
        scrape_link = scrape_link[0]
    
        ethereum_ticker = re.findall(r'coinbase-pro:ethusd":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:ethusd":+\d+', scrape_link)  
        allowance = re.findall(r'remaining":+\d+', scrape_link)
        
        ethereum_price = re.findall(r'\d+\.+\d+', ethereum_ticker[0]) or re.findall(r'\d+', ethereum_ticker[0])
        allowance = re.findall(r'\d+', allowance[0])
        
        ethereum_price = ethereum_price[0]
        allowance = allowance[0]

        ethereum_price = float(ethereum_price)
        allowance = int(allowance)
        
        ethereum_historic.append(ethereum_price)
        
        ethereum_historic_set = set(ethereum_historic)
        
        if len(ethereum_historic_set) == 10 or len(ethereum_historic) >100:
            ethereum_historic.pop(0)

        axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
        axes1.set_title("Ethereum Price")
        axes1.set_xlabel("Iterations")
        axes1.set_ylabel("In Dollars")

        if ethereum_historic[-1] not in ethereum_list:
            ethereum_list.append(ethereum_historic[-1])
        
        if len(ethereum_list) == 1:
            axes1.plot(ethereum_historic, "#7f7fff")
        if len(ethereum_list) >= 2:
            if ethereum_list[-1] > ethereum_list[-2]:
                axes1.plot(ethereum_historic, color = "#00870b")
            elif ethereum_list[-1] < ethereum_list[-2]:
                axes1.plot(ethereum_historic, color = "#ff0000")
        
        axes1.ticklabel_format(useOffset=False, style='plain')

        plt.draw()
    
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(17)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(7)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(2)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)

        plt.pause(3)
    return    
    
def ripple():
    
    """This is the Ripple webscrapper"""
    
    ripple_historic = []
    ripple_list = []
    fig = plt.figure()

    while True:
        fig.clf()
        scrape = requests.get("https://api.cryptowat.ch/markets/prices")
        scrape_content = html.fromstring(scrape.content)
        scrape_link = scrape_content.xpath("text()")
        scrape_link = scrape_link[0]
        
        bitcoin_ticker = re.findall(r'coinbase-pro:btcusd":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:btcusd":+\d+', scrape_link)   
        ripple_ticker = re.findall(r'binance:xrpbtc":+\d+\.+\d+', scrape_link)
        allowance = re.findall(r'remaining":+\d+', scrape_link)
        
        bitcoin_price = re.findall(r'\d+\.+\d+', bitcoin_ticker[0]) or re.findall(r'\d+', bitcoin_ticker[0])
        ripple_price = re.findall(r'\d+\.+\d+', ripple_ticker[0]) or re.findall(r'\d+', ripple_ticker[0])
        allowance = re.findall(r'\d+', allowance[0])
 
        bitcoin_price = bitcoin_price[0]     
        ripple_price = ripple_price[0]
        allowance = allowance[0]
        
        bitcoin_price = float(bitcoin_price)
        ripple_price = float(ripple_price) * bitcoin_price
        allowance = int(allowance)
        
        ripple_historic.append(ripple_price)
        
        ripple_historic_set = set(ripple_historic)
        
        if len(ripple_historic_set) == 10 or len(ripple_historic) >100:
            ripple_historic.pop(0)

        axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
        axes1.set_title("Ripple Price")
        axes1.set_xlabel("Iterations")
        axes1.set_ylabel("In Dollars")

        if ripple_historic[-1] not in ripple_list:
            ripple_list.append(ripple_historic[-1])
        
        if len(ripple_list) == 1:
            axes1.plot(ripple_historic, "#7f7fff")
        if len(ripple_list) >= 2:
            if ripple_list[-1] > ripple_list[-2]:
                axes1.plot(ripple_historic, color = "#00870b")
            elif ripple_list[-1] < ripple_list[-2]:
                axes1.plot(ripple_historic, color = "#ff0000")
        
        axes1.ticklabel_format(useOffset=False, style='plain')

        plt.draw()
    
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(17)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(7)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(2)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)

        plt.pause(3)
    return       
    
def substratum():
    
    """This is the Substratum webscrapper"""
    
    substratum_historic = []
    substratum_list = []
    fig = plt.figure()

    while True:
        plt.clf()
        scrape = requests.get("https://api.cryptowat.ch/markets/prices")
        scrape_content = html.fromstring(scrape.content)
        scrape_link = scrape_content.xpath("text()")
        scrape_link = scrape_link[0]
    
        bitcoin_ticker = re.findall(r'coinbase-pro:btcusd":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:btcusd":+\d+', scrape_link)
        substratum_ticker = re.findall(r'binance:subbtc":+\d+\.+\d+', scrape_link) 
        allowance = re.findall(r'remaining":+\d+', scrape_link)
        
        bitcoin_price = re.findall(r'\d+\.+\d+', bitcoin_ticker[0]) or re.findall(r'\d+', bitcoin_ticker[0])
        substratum_price = re.findall(r'\d+\.+\d+', substratum_ticker[0]) or re.findall(r'\d+', substratum_ticker[0])
        allowance = re.findall(r'\d+', allowance[0])
        
        bitcoin_price = bitcoin_price[0]  
        substratum_price = substratum_price[0]
        allowance = allowance[0]
        
        bitcoin_price = float(bitcoin_price)
        substratum_price = float(substratum_price) * bitcoin_price
        allowance = int(allowance)
        
        substratum_historic.append(substratum_price)
        
        substratum_historic_set = set(substratum_historic)

        if len(substratum_historic_set) == 10 or len(substratum_historic) >100:
            substratum_historic.pop(0)

        axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
        axes1.set_title("Substratum Price")
        axes1.set_xlabel("Iterations")
        axes1.set_ylabel("In Dollars")

        if substratum_historic[-1] not in substratum_list:
            substratum_list.append(substratum_historic[-1])
        
        if len(substratum_list) == 1:
            axes1.plot(substratum_historic, "#7f7fff")
        if len(substratum_list) >= 2:
            if substratum_list[-1] > substratum_list[-2]:
                axes1.plot(substratum_historic, color = "#00870b")
            elif substratum_list[-1] < substratum_list[-2]:
                axes1.plot(substratum_historic, color = "#ff0000")
        
        axes1.ticklabel_format(useOffset=False, style='plain')

        plt.draw()
        
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(17)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(7)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(2)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)
    
        plt.pause(3)    
    return  

#This is the very first class, and it helps initialising the script
class InvestMan(tk.Tk):
    
    """This helps the program use tkinter to initialise the project! jeej :)
    """
    def __init__(self, *args, **kwargs):
        
        #Inititialise application
        tk.Tk.__init__(self, *args, **kwargs)
        
        #Title shown in bar, not using a logo as this would be an addition to a future version
        tk.Tk.wm_title(self, "InvestMan App")
        
        #Containersizes 
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #Defining self function
        self.frames = {}
        
        #Pages being used in the application (first one is startup)
        for F in (
                
                StartPage, BTCgraph, ETHgraph, XRPgraph, SUBgraph, 
                  BTCgraphminute, BTCgraphfifteen, BTCgraphhour, BTCgraph4hour,
                  ETHgraphminute, ETHgraphfifteen, ETHgraphhour, ETHgraph4hour,
                  XRPgraphminute, XRPgraphfifteen, XRPgraphhour, XRPgraph4hour,
                  SUBgraphminute, SUBgraphfifteen, SUBgraphhour, SUBgraph4hour):

            #container and frame selector
            frame = F(container, self)

            #current frame selector
            self.frames[F] = frame
            
            #Grid of frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        #Show frame (startpage initialise)
        self.show_frame(StartPage)

    def show_frame(self, cont):
        #Initialising frame and showing
        frame = self.frames[cont]
        frame.tkraise()
      
class StartPage(tk.Frame):
    
    """This is the landingpage of the InvestMan application, on this page the user can decide to 
    subpages"""
    
    #Initialise the page when startup
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the InvestMan App!", font=LARGE_FONT)
        label.pack(pady=10,padx=20)

        #Buttons lead to new subpages (lamda is used as a temporary function)
        button = ttk.Button(self, text="Bitcoin graphs",
                            command=lambda: controller.show_frame(BTCgraph))
        button.pack()
        button2 = ttk.Button(self, text="Ethereum graphs",
                            command=lambda: controller.show_frame(ETHgraph))
        button2.pack()
        button3 = ttk.Button(self, text="Ripple graphs",
                            command=lambda: controller.show_frame(XRPgraph))
        button3.pack()
        button4 = ttk.Button(self, text="Substratum graphs",
                            command=lambda: controller.show_frame(SUBgraph))
        button4.pack()
        
class BTCgraph(tk.Frame): 
    
    """Overview page for the Bitcoin charts"""
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bitcoin (BTC) Graphs", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button0 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button0.pack()
        button1 = ttk.Button(self, text="Minute Chart",
                            command=lambda: controller.show_frame(BTCgraphminute))
        button1.pack()
        button2 = ttk.Button(self, text="15 Minute Chart",
                            command=lambda: controller.show_frame(BTCgraphfifteen))
        button2.pack()
        button3 = ttk.Button(self, text="Hourly Chart",
                            command=lambda: controller.show_frame(BTCgraphhour))
        button3.pack()
        button4 = ttk.Button(self, text="4 Hour Chart",
                            command=lambda: controller.show_frame(BTCgraph4hour))
        button4.pack()
        
        button5 = ttk.Button(self, text="Real Time Bitcoin Chart (does work, but software needs to restart after using, sorry!)",
                            command=lambda: controller.show_frame(bitcoin()))
        button5.pack()
        
class BTCgraphminute(tk.Frame):
    
    """"Show an updating chart (each iteration is one minute)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BTC Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Bitcoin Charts",
                            command=lambda: controller.show_frame(BTCgraph))
        button1.pack()

        count = 27938 
        count_h = 27939
        count_l = 27940
        bitcoin_minute_list = []
        bitcoin_minute_list_h = []
        bitcoin_minute_list_l = []
    
        while len(bitcoin_minute_list) <= 499: 
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
            bitcoin_minute_list.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_h])
            bitcoin_minute_list_h.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_l])
            bitcoin_minute_list_l.append(bitcoin_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(bitcoin_minute_list, "#7f7fff", linewidth =1)
        a.plot(bitcoin_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Bitcoin Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Minute)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class BTCgraphfifteen(tk.Frame):
    
    """"Show an updating chart (each iteration is fifteen minutes)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BTC 15 Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Bitcoin Charts",
                            command=lambda: controller.show_frame(BTCgraph))
        button1.pack()

        count = 39943 
        count_h = 39944
        count_l = 39945
        bitcoin_fifteen_list = []
        bitcoin_fifteen_list_h = []
        bitcoin_fifteen_list_l = []
    
        while len(bitcoin_fifteen_list) <= 499: 
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
            bitcoin_fifteen_list.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_h])
            bitcoin_fifteen_list_h.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_l])
            bitcoin_fifteen_list_l.append(bitcoin_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(bitcoin_fifteen_list, "#7f7fff", linewidth =1)
        a.plot(bitcoin_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Bitcoin 15 Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 15 Minutes)")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class BTCgraphhour(tk.Frame):
    
    """"Show an updating chart (each iteration is one hour)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BTC Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Bitcoin Charts",
                            command=lambda: controller.show_frame(BTCgraph))
        button1.pack()

        count = 20938 
        count_h = 20939
        count_l = 20940
        bitcoin_hour_list = []
        bitcoin_hour_list_h = []
        bitcoin_hour_list_l = []
    
        while len(bitcoin_hour_list) <= 499: 
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
            bitcoin_hour_list.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_h])
            bitcoin_hour_list_h.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_l])
            bitcoin_hour_list_l.append(bitcoin_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(bitcoin_hour_list, "#7f7fff", linewidth =1)
        a.plot(bitcoin_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Bitcoin Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Hour)")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class BTCgraph4hour(tk.Frame):

    """"Show an updating chart (each iteration is 4 hours)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BTC 4 Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Bitcoin Charts",
                            command=lambda: controller.show_frame(BTCgraph))
        button1.pack()
        
        count = 1 
        count_h = 2
        count_l = 3
        bitcoin_4hour_list = []
        bitcoin_4hour_list_h = []
        bitcoin_4hour_list_l = []
    
        while len(bitcoin_4hour_list) <= 499: 
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
            bitcoin_4hour_list.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_h])
            bitcoin_4hour_list_h.append(bitcoin_ohlc_element)
        
            bitcoin_ohlc_element = float(bitcoin_ohlc_link[count_l])
            bitcoin_4hour_list_l.append(bitcoin_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(bitcoin_4hour_list, "#7f7fff", linewidth =1)
        a.plot(bitcoin_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_4hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Bitcoin 4 Hours Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 4 Hours)")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class ETHgraph(tk.Frame):
    
    """Overview page for the Ethereum charts"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ethereum (ETH) Graphs", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button0 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button0.pack()
        button1 = ttk.Button(self, text="Minute Chart",
                            command=lambda: controller.show_frame(ETHgraphminute))
        button1.pack()
        button2 = ttk.Button(self, text="15 Minute Chart",
                            command=lambda: controller.show_frame(ETHgraphfifteen))
        button2.pack()
        button3 = ttk.Button(self, text="Hourly Chart",
                            command=lambda: controller.show_frame(ETHgraphhour))
        button3.pack()
        button4 = ttk.Button(self, text="4 Hour Chart",
                            command=lambda: controller.show_frame(ETHgraph4hour))
        button4.pack()    

        button5 = ttk.Button(self, text="Real Time Ethereum Chart (does work, but software needs to restart after using, sorry!)",
                            command=lambda: controller.show_frame(ethereum()))
        button5.pack()

class ETHgraphminute(tk.Frame):
    
    """"Show an updating chart (each iteration is one minute)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ETH Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ethereum Charts",
                            command=lambda: controller.show_frame(ETHgraph))
        button1.pack()
        
        count = 26769
        count_h = 26770
        count_l = 26771
        ethereum_minute_list = []
        ethereum_minute_list_h = []
        ethereum_minute_list_l = []
    
        while len(ethereum_minute_list) <= 499: 
            ethereum_ohlc_element = float(ethereum_ohlc_link[count])
            ethereum_minute_list.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_h])
            ethereum_minute_list_h.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_l])
            ethereum_minute_list_l.append(ethereum_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ethereum_minute_list, "#7f7fff", linewidth =1)
        a.plot(ethereum_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Ethereum Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Minute)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class ETHgraphfifteen(tk.Frame):

    """"Show an updating chart (each iteration is fifteen minutes)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ETH 15 Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ethereum Charts",
                            command=lambda: controller.show_frame(ETHgraph))
        button1.pack()

        count = 38263
        count_h = 38264
        count_l = 38265
        ethereum_fifteen_list = []
        ethereum_fifteen_list_h = []
        ethereum_fifteen_list_l = []
    
        while len(ethereum_fifteen_list) <= 499: 
            ethereum_ohlc_element = float(ethereum_ohlc_link[count])
            ethereum_fifteen_list.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_h])
            ethereum_fifteen_list_h.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_l])
            ethereum_fifteen_list_l.append(ethereum_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ethereum_fifteen_list, "#7f7fff", linewidth =1)
        a.plot(ethereum_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Ethereum 15 Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 15 Minutes)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class ETHgraphhour(tk.Frame):
    
    """"Show an updating chart (each iteration is one hour)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ETH Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ethereum Charts",
                            command=lambda: controller.show_frame(ETHgraph))
        button1.pack()

        count = 19769
        count_h = 19770
        count_l = 19771
        ethereum_hour_list = []
        ethereum_hour_list_h = []
        ethereum_hour_list_l = []
    
        while len(ethereum_hour_list) <= 499: 
            ethereum_ohlc_element = float(ethereum_ohlc_link[count])
            ethereum_hour_list.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_h])
            ethereum_hour_list_h.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_l])
            ethereum_hour_list_l.append(ethereum_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ethereum_hour_list, "#7f7fff", linewidth =1)
        a.plot(ethereum_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Ethereum Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Hour)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class ETHgraph4hour(tk.Frame):
    
    """"Show an updating chart (each iteration is 4 hours)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ETH 4 Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ethereum Charts",
                            command=lambda: controller.show_frame(ETHgraph))
        button1.pack()

        count = 1
        count_h = 2
        count_l = 3
        ethereum_4hour_list = []
        ethereum_4hour_list_h = []
        ethereum_4hour_list_l = []
    
        while len(ethereum_4hour_list) <= 499: 
            ethereum_ohlc_element = float(ethereum_ohlc_link[count])
            ethereum_4hour_list.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_h])
            ethereum_4hour_list_h.append(ethereum_ohlc_element)
        
            ethereum_ohlc_element = float(ethereum_ohlc_link[count_l])
            ethereum_4hour_list_l.append(ethereum_ohlc_element)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ethereum_4hour_list, "#7f7fff", linewidth =1)
        a.plot(ethereum_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_4hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Ethereum 4 Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 4 Hours)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class XRPgraph(tk.Frame):
    
    """Overview page for the Ripple charts"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ripple (XRP) Graphs", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button0 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button0.pack()
        button1 = ttk.Button(self, text="Minute Chart",
                            command=lambda: controller.show_frame(XRPgraphminute))
        button1.pack()
        button2 = ttk.Button(self, text="15 Minute Chart",
                            command=lambda: controller.show_frame(XRPgraphfifteen))
        button2.pack()
        button3 = ttk.Button(self, text="Hourly Chart",
                            command=lambda: controller.show_frame(XRPgraphhour))
        button3.pack()
        button4 = ttk.Button(self, text="4 Hour Chart",
                            command=lambda: controller.show_frame(XRPgraph4hour))
        button4.pack()
        
        button5 = ttk.Button(self, text="Real Time Ripple Chart (does work, but software needs to restart after using, sorry!)",
                            command=lambda: controller.show_frame(ripple()))
        button5.pack()

class XRPgraphminute(tk.Frame):

    """"Show an updating chart (each iteration is one minute)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="XRP Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ripple Charts",
                            command=lambda: controller.show_frame(XRPgraph))
        button1.pack()
        
        count = 25306
        count_h = 25307
        count_l = 25308
        ripple_minute_list = []
        ripple_minute_list_h = []
        ripple_minute_list_l = []
    
        while len(ripple_minute_list) <= 499: 
            ripple_ohlc_element = float(ripple_ohlc_link[count])
            ripple_minute_list.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_h])
            ripple_minute_list_h.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_l])
            ripple_minute_list_l.append(ripple_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ripple_minute_list, "#7f7fff", linewidth =1)
        a.plot(ripple_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Ripple Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Minute)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class XRPgraphfifteen(tk.Frame):

    """"Show an updating chart (each iteration is fifteen minutes)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="XRP 15 Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ripple Charts",
                            command=lambda: controller.show_frame(XRPgraph))
        button1.pack()

        count = 35064
        count_h = 35065
        count_l = 35066
        ripple_fifteen_list = []
        ripple_fifteen_list_h = []
        ripple_fifteen_list_l = []
    
        while len(ripple_fifteen_list) <= 499: 
            ripple_ohlc_element = float(ripple_ohlc_link[count])
            ripple_fifteen_list.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_h])
            ripple_fifteen_list_h.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_l])
            ripple_fifteen_list_l.append(ripple_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ripple_fifteen_list, "#7f7fff", linewidth =1)
        a.plot(ripple_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])

        a.set_title("Ripple 15 Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 15 Minutes)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True) 

class XRPgraphhour(tk.Frame):
    
    """"Show an updating chart (each iteration is one hour)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="XRP Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ripple Charts",
                            command=lambda: controller.show_frame(XRPgraph))
        button1.pack()

        count = 18306
        count_h = 18307
        count_l = 18308
        ripple_hour_list = []
        ripple_hour_list_h = []
        ripple_hour_list_l = []
    
        while len(ripple_hour_list) <= 499: 
            ripple_ohlc_element = float(ripple_ohlc_link[count])
            ripple_hour_list.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_h])
            ripple_hour_list_h.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_l])
            ripple_hour_list_l.append(ripple_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ripple_hour_list, "#7f7fff", linewidth =1)
        a.plot(ripple_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Ripple Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Hour)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True) 
        
class XRPgraph4hour(tk.Frame):
    
    """"Show an updating chart (each iteration is 4 hours)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="XRP 4 Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Ripple Charts",
                            command=lambda: controller.show_frame(XRPgraph))
        button1.pack()

        count = 1
        count_h = 2
        count_l = 3
        ripple_4hour_list = []
        ripple_4hour_list_h = []
        ripple_4hour_list_l = []
    
        while len(ripple_4hour_list) <= 499: 
            ripple_ohlc_element = float(ripple_ohlc_link[count])
            ripple_4hour_list.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_h])
            ripple_4hour_list_h.append(ripple_ohlc_element * bitcoin_price)
        
            ripple_ohlc_element = float(ripple_ohlc_link[count_l])
            ripple_4hour_list_l.append(ripple_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(ripple_4hour_list, "#7f7fff", linewidth =1)
        a.plot(ripple_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_4hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Ripple 4 Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 4 Hours)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True) 
        
class SUBgraph(tk.Frame):

    """Overview page for the Substratum charts"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Substratum (SUB) Graphs", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button0 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button0.pack()
        button1 = ttk.Button(self, text="Minute Chart",
                            command=lambda: controller.show_frame(SUBgraphminute))
        button1.pack()
        button2 = ttk.Button(self, text="15 Minute Chart",
                            command=lambda: controller.show_frame(SUBgraphfifteen))
        button2.pack()
        button3 = ttk.Button(self, text="Hourly Chart",
                            command=lambda: controller.show_frame(SUBgraphhour))
        button3.pack()
        button4 = ttk.Button(self, text="4 Hour Chart",
                            command=lambda: controller.show_frame(SUBgraph4hour))
        button4.pack()

        button5 = ttk.Button(self, text="Real Time Substratum Chart (does work, but software needs to restart after using, sorry!)",
                            command=lambda: controller.show_frame(substratum()))
        button5.pack()

class SUBgraphminute(tk.Frame):

    """"Show an updating chart (each iteration is one minute)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SUB Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Substratum Charts",
                            command=lambda: controller.show_frame(SUBgraph))
        button1.pack()

        count = 24907
        count_h = 24908
        count_l = 24909
        substratum_minute_list = []
        substratum_minute_list_h = []
        substratum_minute_list_l = []
    
        while len(substratum_minute_list) <= 499: 
            substratum_ohlc_element = float(substratum_ohlc_link[count])
            substratum_minute_list.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_h])
            substratum_minute_list_h.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_l])
            substratum_minute_list_l.append(substratum_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(substratum_minute_list, "#7f7fff", linewidth =1)
        a.plot(substratum_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Substratum Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Minute)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class SUBgraphfifteen(tk.Frame):

    """"Show an updating chart (each iteration is fifteen minutes)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SUB 15 Minute Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Substratum Charts",
                            command=lambda: controller.show_frame(SUBgraph))
        button1.pack()

        count = 33825
        count_h = 33826
        count_l = 33827
        substratum_fifteen_list = []
        substratum_fifteen_list_h = []
        substratum_fifteen_list_l = []
    
        while len(substratum_fifteen_list) <= 499: 
            substratum_ohlc_element = float(substratum_ohlc_link[count])
            substratum_fifteen_list.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_h])
            substratum_fifteen_list_h.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_l])
            substratum_fifteen_list_l.append(substratum_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(substratum_fifteen_list, "#7f7fff", linewidth =1)
        a.plot(substratum_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Substratum 15 Minute Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 15 Minutes)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class SUBgraphhour(tk.Frame):

    """"Show an updating chart (each iteration is one hour)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SUB Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Substratum Charts",
                            command=lambda: controller.show_frame(SUBgraph))
        button1.pack()

        count = 18061
        count_h = 18062
        count_l = 18063
        substratum_hour_list = []
        substratum_hour_list_h = []
        substratum_hour_list_l = []
    
        while len(substratum_hour_list) <= 499: 
            substratum_ohlc_element = float(substratum_ohlc_link[count])
            substratum_hour_list.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_h])
            substratum_hour_list_h.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_l])
            substratum_hour_list_l.append(substratum_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(substratum_hour_list, "#7f7fff", linewidth =1)
        a.plot(substratum_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Substratum Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every Hour)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
class SUBgraph4hour(tk.Frame):

    """"Show an updating chart (each iteration is 4 hours)"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="SUB 4 Hour Chart", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text="Back to Substratum Charts",
                            command=lambda: controller.show_frame(SUBgraph))
        button1.pack()

        count = 1
        count_h = 2
        count_l = 3
        substratum_4hour_list = []
        substratum_4hour_list_h = []
        substratum_4hour_list_l = []
    
        while len(substratum_4hour_list) <= 499: 
            substratum_ohlc_element = float(substratum_ohlc_link[count])
            substratum_4hour_list.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_h])
            substratum_4hour_list_h.append(substratum_ohlc_element * bitcoin_price)
        
            substratum_ohlc_element = float(substratum_ohlc_link[count_l])
            substratum_4hour_list_l.append(substratum_ohlc_element * bitcoin_price)
        
            count += 7 
            count_h += 7
            count_l += 7
            
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_axes([0.1,0.1,0.8,0.8])
        a.plot(substratum_4hour_list, "#7f7fff", linewidth =1)
        a.plot(substratum_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_4hour_list_l, "#ff0000", linewidth =0.5)
               
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        a.legend(handles=[blue_line, green_line, red_line])
    
        a.set_title("Substratum 4 Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 4 Hours)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def Runapp (): # Run the application
    app = InvestMan()
    app.mainloop()
    

    
