# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:27:02 2019

@author: Gijs Koenders
"""

import requests
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches

ethereum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/ethusd/ohlc")
ethereum_ohlc_link = ethereum_ohlc_link.text
ethereum_ohlc_link = ethereum_ohlc_link.split(",")

def ethereum_minute():
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
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_minute_list)
    axes.plot(ethereum_minute_list_h, "#00870b")
    axes.plot(ethereum_minute_list_l, "#ff0000")
              
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ethereum minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    
    return

def ethereum_fifteen():
    count = 38263
    count_h = 38264
    count_l = 38265
    ethereum_fifteen_list = []
    ethereum_minute_list_h = []
    ethereum_minute_list_l = []
    
    while len(ethereum_fifteen_list) <= 499: 
        ethereum_ohlc_element = float(ethereum_ohlc_link[count])
        ethereum_fifteen_list.append(ethereum_ohlc_element)
        
        ethereum_ohlc_element = float(ethereum_ohlc_link[count_h])
        ethereum_minute_list_h.append(ethereum_ohlc_element)
        
        ethereum_ohlc_element = float(ethereum_ohlc_link[count_l])
        ethereum_minute_list_l.append(ethereum_ohlc_element)
        
        count += 7 
        count_h += 7
        count_l += 7
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_fifteen_list)
    axes.plot(ethereum_minute_list_h, "#00870b")
    axes.plot(ethereum_minute_list_l, "#ff0000")
              
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ethereum 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def ethereum_hour():
    count = 19769
    count_h = 19770
    count_l = 19771
    ethereum_hour_list = []
    ethereum_minute_list_h = []
    ethereum_minute_list_l = []
    
    while len(ethereum_hour_list) <= 499: 
        ethereum_ohlc_element = float(ethereum_ohlc_link[count])
        ethereum_hour_list.append(ethereum_ohlc_element)
        
        ethereum_ohlc_element = float(ethereum_ohlc_link[count_h])
        ethereum_minute_list_h.append(ethereum_ohlc_element)
        
        ethereum_ohlc_element = float(ethereum_ohlc_link[count_l])
        ethereum_minute_list_l.append(ethereum_ohlc_element)
        
        count += 7 
        count_h += 7
        count_l += 7
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_hour_list)
    axes.plot(ethereum_minute_list_h, "#00870b")
    axes.plot(ethereum_minute_list_l, "#ff0000")
              
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ethereum 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def ethereum_4hour():
    count = 1
    count_h = 2
    count_l = 3
    ethereum_4hour_list = []
    ethereum_minute_list_h = []
    ethereum_minute_list_l = []
    
    while len(ethereum_4hour_list) <= 499: 
        ethereum_ohlc_element = float(ethereum_ohlc_link[count])
        ethereum_4hour_list.append(ethereum_ohlc_element)
        
        ethereum_ohlc_element = float(ethereum_ohlc_link[count_h])
        ethereum_minute_list_h.append(ethereum_ohlc_element)
        
        ethereum_ohlc_element = float(ethereum_ohlc_link[count_l])
        ethereum_minute_list_l.append(ethereum_ohlc_element)
        
        count += 7 
        count_h += 7
        count_l += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_4hour_list)
    axes.plot(ethereum_minute_list_h, "#00870b")
    axes.plot(ethereum_minute_list_l, "#ff0000")
              
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ethereum 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return

ethereum_minute()
ethereum_fifteen()
ethereum_hour()
ethereum_4hour()