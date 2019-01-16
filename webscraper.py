# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:24:19 2018

@author: Gijs Koenders
"""

from lxml import html
import requests
from time import sleep
import re
from matplotlib import pyplot as plt

def bitcoin():
    
    """The webscraper calls realtime price information for cryptocurrencies"""
    bitcoin_historic = []
    bitcoin_list = []
    
    while True:
        scrape = requests.get("https://api.cryptowat.ch/markets/prices")
        scrape_content = html.fromstring(scrape.content)
        scrape_link = scrape_content.xpath("text()")
        scrape_link = scrape_link[0]
    
        bitcoin_ticker = re.findall(r'coinbase-pro:btc":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:btcusd":+\d+', scrape_link)  
        allowance = re.findall(r'remaining":+\d+', scrape_link)
        
        bitcoin_price = re.findall(r'\d+\.+\d+', bitcoin_ticker[0]) or re.findall(r'\d+', bitcoin_ticker[0])
        allowance = re.findall(r'\d+', allowance[0])
        
        bitcoin_price = bitcoin_price[0]
        allowance = allowance[0]

        bitcoin_price = float(bitcoin_price)
        allowance = int(allowance)
        
        bitcoin_historic.append(bitcoin_price)
        
        bitcoin_historic_set = set(bitcoin_historic)
        
        if len(bitcoin_historic_set) == 10 or len(bitcoin_historic) >100:
            bitcoin_historic.pop(0)

        fig = plt.figure()
        axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
        axes1.set_title("Bitcoin Price")
        axes1.set_xlabel("Iterations")
        axes1.set_ylabel("In Dollars")

        if bitcoin_historic[-1] not in bitcoin_list:
            bitcoin_list.append(bitcoin_historic[-1])
        
        if len(bitcoin_list) == 1:
            axes1.plot(bitcoin_historic,"#7f7fff")
        if len(bitcoin_list) >= 2:
            if bitcoin_list[-1] > bitcoin_list[-2]:
                axes1.plot(bitcoin_historic, color = "#00870b")
            elif bitcoin_list[-1] < bitcoin_list[-2]:
                axes1.plot(bitcoin_historic, color = "#ff0000")
        
        axes1.ticklabel_format(useOffset=False, style='plain')

        plt.show()
    
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(20)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(10)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(2)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)
    return 

def ethereum():
    
    """The webscraper calls realtime price information for cryptocurrencies"""
    ethereum_historic = []
    ethereum_list = []
    
    while True:
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

        fig = plt.figure()
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

        plt.show()
    
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(20)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(10)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(2)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)
    
    return    
    
def ripple():
    
    """The webscraper calls realtime price information for cryptocurrencies"""
    ripple_historic = []
    ripple_list = []
    
    while True:
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

        fig = plt.figure()
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

        plt.show()
    
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(20)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(10)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(5)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)
    
    return       
    
def substratum():
    
    """The webscraper calls realtime price information for cryptocurrencies"""
    substratum_historic = []
    substratum_list = []
    
    while True:
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

        fig = plt.figure()
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

        plt.show()
        
        if allowance < 400000000:
            print("Prices update every 20 seconds")
            print("")
            sleep(20)
        
        elif allowance < 1000000000:
            print("Prices update every 10 seconds")
            print("")
            sleep(10)
        
        elif allowance < 8000000000:
            print("Prices update every 5 seconds")
            print("")
            sleep(2)
        
        elif allowance == 0 or allowance < 0: 
            print("No new requests possible, wait till the hour has passed to start fresh!")
            sleep(60)
    
    return           

bitcoin()
ethereum()
ripple()
substratum()