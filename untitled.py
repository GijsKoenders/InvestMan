# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 21:24:19 2019

@author: gijsd
"""

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
matplotlib.use("TkAgg")
import tkinter as tk
from tkinter import ttk
import requests
from lxml import html

LARGE_FONT= ("Verdana", 12)

bitcoin_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/btcusd/ohlc")
bitcoin_ohlc_link = bitcoin_ohlc_link.text
bitcoin_ohlc_link = bitcoin_ohlc_link.split(",")
bitcoin_price = float(bitcoin_ohlc_link[-7])

ethereum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/ethusd/ohlc")
ethereum_ohlc_link = ethereum_ohlc_link.text
ethereum_ohlc_link = ethereum_ohlc_link.split(",")

ripple_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/xrpbtc/ohlc")
ripple_ohlc_link = ripple_ohlc_link.text
ripple_ohlc_link = ripple_ohlc_link.split(",")

substratum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/subbtc/ohlc")
substratum_ohlc_link = substratum_ohlc_link.text
substratum_ohlc_link = substratum_ohlc_link.split(",")

scrape = requests.get("https://api.cryptowat.ch/markets/prices")
scrape_content = html.fromstring(scrape.content)
scrape_link = scrape_content.xpath("text()")
scrape_link = scrape_link[0]

bitcoin_historic = []
ethereum_historic = []
ripple_historic = []
substratum_historic = []

bitcoin_list = []
ethereum_list = []
ripple_list = []
substratum_list = []
 
class InvestMan(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "InvestMan App")
            
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
                
                StartPage, BTCgraph, ETHgraph, XRPgraph, SUBgraph, 
                  BTCgraphminute, BTCgraphfifteen, BTCgraphhour, BTCgraph4hour,
                  ETHgraphminute, ETHgraphfifteen, ETHgraphhour, ETHgraph4hour,
                  XRPgraphminute, XRPgraphfifteen, XRPgraphhour, XRPgraph4hour,
                  SUBgraphminute, SUBgraphfifteen, SUBgraphhour, SUBgraph4hour):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
      
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=20)

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
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3])
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
class BTCgraphminute(tk.Frame):

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
        a.plot(bitcoin_minute_list, linewidth =1)
        a.plot(bitcoin_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(bitcoin_fifteen_list, linewidth =1)
        a.plot(bitcoin_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(bitcoin_hour_list, linewidth =1)
        a.plot(bitcoin_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(bitcoin_4hour_list, linewidth =1)
        a.plot(bitcoin_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(bitcoin_4hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class ETHgraphminute(tk.Frame):

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
        a.plot(ethereum_minute_list, linewidth =1)
        a.plot(ethereum_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(ethereum_fifteen_list, linewidth =1)
        a.plot(ethereum_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(ethereum_hour_list, linewidth =1)
        a.plot(ethereum_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(ethereum_4hour_list, linewidth =1)
        a.plot(ethereum_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ethereum_4hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class XRPgraphminute(tk.Frame):

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
        a.plot(ripple_minute_list, linewidth =1)
        a.plot(ripple_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(ripple_fifteen_list, linewidth =1)
        a.plot(ripple_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(ripple_hour_list, linewidth =1)
        a.plot(ripple_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(ripple_4hour_list, linewidth =1)
        a.plot(ripple_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(ripple_4hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class SUBgraphminute(tk.Frame):

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
        a.plot(substratum_minute_list, linewidth =1)
        a.plot(substratum_minute_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_minute_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(substratum_fifteen_list, linewidth =1)
        a.plot(substratum_fifteen_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_fifteen_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(substratum_hour_list, linewidth =1)
        a.plot(substratum_hour_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_hour_list_l, "#ff0000", linewidth =0.5)
    
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
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
        a.plot(substratum_4hour_list, linewidth =1)
        a.plot(substratum_4hour_list_h, "#00870b", linewidth =0.5)
        a.plot(substratum_4hour_list_l, "#ff0000", linewidth =0.5)
               
        blue_line = mpatches.Patch(color='blue', label='Open')
        green_line = mpatches.Patch(color='green', label='Highest')
        red_line = mpatches.Patch(color='red', label='Lowest')
        plt.legend(handles=[blue_line, green_line, red_line])
        plt.style.use("seaborn-darkgrid")
    
        a.set_title("Substratum 4 Hour Chart")
        a.set_ylabel("Price in Dollars")
        a.set_xlabel("Iterations (Updates Every 4 Hours)")
    
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = InvestMan()
app.mainloop()
