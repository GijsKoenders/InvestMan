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

ripple_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/xrpbtc/ohlc")
ripple_ohlc_link = ripple_ohlc_link.text
ripple_ohlc_link = ripple_ohlc_link.split(",")

def ripple_minute():
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
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_minute_list)
    axes.plot(ripple_minute_list_h, "#00870b")
    axes.plot(ripple_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ripple minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    
    return

def ripple_fifteen():
    count = 35064
    count_h = 35065
    count_l = 35066
    ripple_fifteen_list = []
    ripple_minute_list_h = []
    ripple_minute_list_l = []
    
    while len(ripple_fifteen_list) <= 499: 
        ripple_ohlc_element = float(ripple_ohlc_link[count])
        ripple_fifteen_list.append(ripple_ohlc_element * bitcoin_price)
        
        ripple_ohlc_element = float(ripple_ohlc_link[count_h])
        ripple_minute_list_h.append(ripple_ohlc_element * bitcoin_price)
        
        ripple_ohlc_element = float(ripple_ohlc_link[count_l])
        ripple_minute_list_l.append(ripple_ohlc_element * bitcoin_price)
        
        count += 7 
        count_h += 7
        count_l += 7
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_fifteen_list)
    axes.plot(ripple_minute_list_h, "#00870b")
    axes.plot(ripple_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ripple 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def ripple_hour():
    count = 18306
    count_h = 18307
    count_l = 18308
    ripple_hour_list = []
    ripple_minute_list_h = []
    ripple_minute_list_l = []
    
    while len(ripple_hour_list) <= 499: 
        ripple_ohlc_element = float(ripple_ohlc_link[count])
        ripple_hour_list.append(ripple_ohlc_element * bitcoin_price)
        
        ripple_ohlc_element = float(ripple_ohlc_link[count_h])
        ripple_minute_list_h.append(ripple_ohlc_element * bitcoin_price)
        
        ripple_ohlc_element = float(ripple_ohlc_link[count_l])
        ripple_minute_list_l.append(ripple_ohlc_element * bitcoin_price)
        
        count += 7 
        count_h += 7
        count_l += 7
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_hour_list)
    axes.plot(ripple_minute_list_h, "#00870b")
    axes.plot(ripple_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ripple 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def ripple_4hour():
    count = 1
    count_h = 2
    count_l = 3
    ripple_4hour_list = []
    ripple_minute_list_h = []
    ripple_minute_list_l = []
    
    while len(ripple_4hour_list) <= 499: 
        ripple_ohlc_element = float(ripple_ohlc_link[count])
        ripple_4hour_list.append(ripple_ohlc_element * bitcoin_price)
        
        ripple_ohlc_element = float(ripple_ohlc_link[count_h])
        ripple_minute_list_h.append(ripple_ohlc_element * bitcoin_price)
        
        ripple_ohlc_element = float(ripple_ohlc_link[count_l])
        ripple_minute_list_l.append(ripple_ohlc_element * bitcoin_price)
        
        count += 7 
        count_h += 7
        count_l += 7
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_4hour_list)
    axes.plot(ripple_minute_list_h, "#00870b")
    axes.plot(ripple_minute_list_l, "#ff0000")
    
    blue_line = mpatches.Patch(color='Blue', label='Open')
    green_line = mpatches.Patch(color='green', label='Highest')
    red_line = mpatches.Patch(color='red', label='Lowest')
    plt.legend(handles=[blue_line, green_line, red_line])
    
    axes.set_title("Ripple 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return

ripple_minute()
ripple_fifteen()
ripple_hour()
ripple_4hour()