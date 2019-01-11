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
bitcoin_price = float(bitcoin_ohlc_link[-7])

substratum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/subbtc/ohlc")
substratum_ohlc_link = substratum_ohlc_link.text
substratum_ohlc_link = substratum_ohlc_link.split(",")

def substratum_minute():
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
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_minute_list)
    axes.plot(substratum_minute_list_h, "#00870b")
    axes.plot(substratum_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Substratum minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    
    return

def substratum_fifteen():
    count = 33825
    count_h = 33826
    count_l = 33827
    substratum_fifteen_list = []
    substratum_minute_list_h = []
    substratum_minute_list_l = []
    
    while len(substratum_fifteen_list) <= 499: 
        substratum_ohlc_element = float(substratum_ohlc_link[count])
        substratum_fifteen_list.append(substratum_ohlc_element * bitcoin_price)
        
        substratum_ohlc_element = float(substratum_ohlc_link[count_h])
        substratum_minute_list_h.append(substratum_ohlc_element * bitcoin_price)
        
        substratum_ohlc_element = float(substratum_ohlc_link[count_l])
        substratum_minute_list_l.append(substratum_ohlc_element * bitcoin_price)
        
        count += 7 
        count_h += 7
        count_l += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_fifteen_list)
    axes.plot(substratum_minute_list_h, "#00870b")
    axes.plot(substratum_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Substratum 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def substratum_hour():
    count = 18061
    count_h = 18062
    count_l = 18063
    substratum_hour_list = []
    substratum_minute_list_h = []
    substratum_minute_list_l = []
    
    while len(substratum_hour_list) <= 499: 
        substratum_ohlc_element = float(substratum_ohlc_link[count])
        substratum_hour_list.append(substratum_ohlc_element * bitcoin_price)
        
        substratum_ohlc_element = float(substratum_ohlc_link[count_h])
        substratum_minute_list_h.append(substratum_ohlc_element * bitcoin_price)
        
        substratum_ohlc_element = float(substratum_ohlc_link[count_l])
        substratum_minute_list_l.append(substratum_ohlc_element * bitcoin_price)
        
        count += 7 
        count_h += 7
        count_l += 7
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_hour_list)
    axes.plot(substratum_minute_list_h, "#00870b")
    axes.plot(substratum_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Substratum 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def substratum_4hour():
    count = 1
    count_h = 2
    count_l = 3
    substratum_4hour_list = []
    substratum_minute_list_h = []
    substratum_minute_list_l = []
    
    while len(substratum_4hour_list) <= 499: 
        substratum_ohlc_element = float(substratum_ohlc_link[count])
        substratum_4hour_list.append(substratum_ohlc_element * bitcoin_price)
        
        substratum_ohlc_element = float(substratum_ohlc_link[count_h])
        substratum_minute_list_h.append(substratum_ohlc_element * bitcoin_price)
        
        substratum_ohlc_element = float(substratum_ohlc_link[count_l])
        substratum_minute_list_l.append(substratum_ohlc_element * bitcoin_price)
        
        count += 7 
        count_h += 7
        count_l += 7
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_4hour_list)
    axes.plot(substratum_minute_list_h, "#00870b")
    axes.plot(substratum_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Substratum 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return

substratum_minute()
substratum_fifteen()
substratum_hour()
substratum_4hour()