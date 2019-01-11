# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:27:02 2019

@author: Gijs Koenders
"""

import requests
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches

bitcoin_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/btcusd/ohlc")
bitcoin_ohlc_link = bitcoin_ohlc_link.text
bitcoin_ohlc_link = bitcoin_ohlc_link.split(",")
bitcoin_price = bitcoin_ohlc_link[-7]

def bitcoin_minute():
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
        
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    
    axes.plot(bitcoin_minute_list, linewidth = 1)
    axes.plot(bitcoin_minute_list_h, "#00870b", linewidth =0.5)
    axes.plot(bitcoin_minute_list_l, "#ff0000", linewidth =0.5)

    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    plt.style.use("seaborn-darkgrid")
    
    axes.set_title("Bitcoin minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    return

def bitcoin_fifteen():
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

    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(bitcoin_fifteen_list, linewidth = 1)
    axes.plot(bitcoin_fifteen_list_h, "#00870b", linewidth =0.5)
    axes.plot(bitcoin_fifteen_list_l, "#ff0000", linewidth =0.5)
              
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    plt.style.use("seaborn-darkgrid")
    
    axes.set_title("Bitcoin 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def bitcoin_hour():
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
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(bitcoin_hour_list, linewidth = 1)
    axes.plot(bitcoin_hour_list_h, "#00870b", linewidth = 0.5)
    axes.plot(bitcoin_hour_list_l, "#ff0000", linewidth = 0.5)
              
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])   
    plt.style.use("seaborn-darkgrid")       
    
    axes.set_title("Bitcoin 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def bitcoin_4hour():
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
        
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(bitcoin_4hour_list, linewidth =1)
    axes.plot(bitcoin_4hour_list_h, "#00870b", linewidth =0.5)
    axes.plot(bitcoin_4hour_list_l, "#ff0000", linewidth =0.5)
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    plt.style.use("seaborn-darkgrid")
              
    axes.set_title("Bitcoin 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return

bitcoin_minute()
bitcoin_fifteen()
bitcoin_hour()
bitcoin_4hour()