import requests
import matplotlib.pyplot as plt 

bitcoin_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/btcusd/ohlc")
bitcoin_ohlc_link = bitcoin_ohlc_link.text
bitcoin_ohlc_link = bitcoin_ohlc_link.split(",")
bitcoin_price = bitcoin_ohlc_link[-7]

ethereum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/ethusd/ohlc")
ethereum_ohlc_link = ethereum_ohlc_link.text
ethereum_ohlc_link = ethereum_ohlc_link.split(",")

ripple_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/xrpbtc/ohlc")
ripple_ohlc_link = ripple_ohlc_link.text
ripple_ohlc_link = ripple_ohlc_link.split(",")

substratum_ohlc_link = requests.get("https://api.cryptowat.ch/markets/binance/subbtc/ohlc")
substratum_ohlc_link = substratum_ohlc_link.text
substratum_ohlc_link = substratum_ohlc_link.split(",")

def bitcoin_minute():
    count = 27938 
    bitcoin_minute_list = []
    
    while len(bitcoin_minute_list) <= 499: 
        bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
        bitcoin_minute_list.append(bitcoin_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(bitcoin_minute_list)
    axes.set_title("Bitcoin minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    
    return

def bitcoin_fifteen():
    count = 39943 
    bitcoin_fifteen_list = []
    
    while len(bitcoin_fifteen_list) <= 499: 
        bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
        bitcoin_fifteen_list.append(bitcoin_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(bitcoin_fifteen_list)
    axes.set_title("Bitcoin 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def bitcoin_hour():
    count = 20938 
    bitcoin_hour_list = []
    
    while len(bitcoin_hour_list) <= 499: 
        bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
        bitcoin_hour_list.append(bitcoin_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(bitcoin_hour_list)
    axes.set_title("Bitcoin 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def bitcoin_4hour():
    count = 1 
    bitcoin_4hour_list = []
    
    while len(bitcoin_4hour_list) <= 499: 
        bitcoin_ohlc_element = float(bitcoin_ohlc_link[count])
        bitcoin_4hour_list.append(bitcoin_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(bitcoin_4hour_list)
    axes.set_title("Bitcoin 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return

def ethereum_minute():
    count = 26769
    ethereum_minute_list = []
    
    while len(ethereum_minute_list) <= 499: 
        ethereum_ohlc_element = float(ethereum_ohlc_link[count])
        ethereum_minute_list.append(ethereum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_minute_list)
    axes.set_title("Ethereum minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    
    return

def ethereum_fifteen():
    count = 38263
    ethereum_fifteen_list = []
    
    while len(ethereum_fifteen_list) <= 499: 
        ethereum_ohlc_element = float(ethereum_ohlc_link[count])
        ethereum_fifteen_list.append(ethereum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_fifteen_list)
    axes.set_title("Ethereum 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def ethereum_hour():
    count = 19769
    ethereum_hour_list = []
    
    while len(ethereum_hour_list) <= 499: 
        ethereum_ohlc_element = float(ethereum_ohlc_link[count])
        ethereum_hour_list.append(ethereum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_hour_list)
    axes.set_title("Ethereum 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def ethereum_4hour():
    count = 1
    ethereum_4hour_list = []
    
    while len(ethereum_4hour_list) <= 499: 
        ethereum_ohlc_element = float(ethereum_ohlc_link[count])
        ethereum_4hour_list.append(ethereum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ethereum_4hour_list)
    axes.set_title("Ethereum 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return

def ripple_minute():
    count = 25306
    ripple_minute_list = []
    
    while len(ripple_minute_list) <= 499: 
        ripple_ohlc_element = float(ripple_ohlc_link[count])
        ripple_minute_list.append(ripple_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_minute_list)
    axes.set_title("Ripple minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    
    return

def ripple_fifteen():
    count = 35064
    ripple_fifteen_list = []
    
    while len(ripple_fifteen_list) <= 499: 
        ripple_ohlc_element = float(ripple_ohlc_link[count])
        ripple_fifteen_list.append(ripple_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_fifteen_list)
    axes.set_title("Ripple 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def ripple_hour():
    count = 18306
    ripple_hour_list = []
    
    while len(ripple_hour_list) <= 499: 
        ripple_ohlc_element = float(ripple_ohlc_link[count])
        ripple_hour_list.append(ripple_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_hour_list)
    axes.set_title("Ripple 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def ripple_4hour():
    count = 1
    ripple_4hour_list = []
    
    while len(ripple_4hour_list) <= 499: 
        ripple_ohlc_element = float(ripple_ohlc_link[count])
        ripple_4hour_list.append(ripple_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(ripple_4hour_list)
    axes.set_title("Ripple 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return

def substratum_minute():
    count = 24907
    substratum_minute_list = []
    
    while len(substratum_minute_list) <= 499: 
        substratum_ohlc_element = float(substratum_ohlc_link[count])
        substratum_minute_list.append(substratum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_minute_list)
    axes.set_title("Substratum minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every minute)")
    
    plt.show()
    
    return

def substratum_fifteen():
    count = 33825
    substratum_fifteen_list = []
    
    while len(substratum_fifteen_list) <= 499: 
        substratum_ohlc_element = float(substratum_ohlc_link[count])
        substratum_fifteen_list.append(substratum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_fifteen_list)
    axes.set_title("Substratum 15 minute chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 15 minutes)")
    
    plt.show()
    
    return

def substratum_hour():
    count = 18061
    substratum_hour_list = []
    
    while len(substratum_hour_list) <= 499: 
        substratum_ohlc_element = float(substratum_ohlc_link[count])
        substratum_hour_list.append(substratum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_hour_list)
    axes.set_title("Substratum 1 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every hour)")
    
    plt.show()
    
    return

def substratum_4hour():
    count = 1
    substratum_4hour_list = []
    
    while len(substratum_4hour_list) <= 499: 
        substratum_ohlc_element = float(substratum_ohlc_link[count])
        substratum_4hour_list.append(substratum_ohlc_element)
        
        count += 7 
    
    fig = plt.figure()
    
    axes = fig.add_axes([0.1,0.1,0.8,0.8])
    axes.plot(substratum_4hour_list)
    axes.set_title("Substratum 4 Hour chart")
    axes.set_ylabel("Price in dollars")
    axes.set_xlabel("Iterations (updates every 4 hours)")
    
    plt.show()
    return



