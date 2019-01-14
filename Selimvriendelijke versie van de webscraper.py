# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:27:02 2019

@author: Gijs Koenders
"""

from lxml import html
import requests
import re

"""The webscraper calls realtime price information for cryptocurrencies"""

#data mining part
scrape = requests.get("https://api.cryptowat.ch/markets/prices")
scrape_content = html.fromstring(scrape.content)
scrape_link = scrape_content.xpath("text()")
scrape_link = scrape_link[0]
        
#select relevant information
bitcoin_ticker = re.findall(r'coinbase-pro:btcusd":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:btcusd":+\d+', scrape_link)
ethereum_ticker = re.findall(r'coinbase-pro:ethusd":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:ethusd":+\d+', scrape_link)
ripple_ticker = re.findall(r'binance:xrpbtc":+\d+\.+\d+', scrape_link) 
substratum_ticker = re.findall(r'binance:subbtc":+\d+\.+\d+', scrape_link) 
cost = re.findall(r'cost":+\d+', scrape_link)    
allowance = re.findall(r'remaining":+\d+', scrape_link)
        
#find current price in list
bitcoin_price = re.findall(r'\d+\.+\d+', bitcoin_ticker[0]) or re.findall(r'\d+', bitcoin_ticker[0])
ethereum_price = re.findall(r'\d+\.+\d+', ethereum_ticker[0]) or re.findall(r'\d+', ethereum_ticker[0])
ripple_price = re.findall(r'\d+\.+\d+', ripple_ticker[0]) or re.findall(r'\d+', ripple_ticker[0])
substratum_price = re.findall(r'\d+\.+\d+', substratum_ticker[0]) or re.findall(r'\d+', substratum_ticker[0])
cost = re.findall(r'\d+', cost[0])
allowance = re.findall(r'\d+', allowance[0])
        
#first element of list for actual price (get out of list to turn into strings)
bitcoin_price = bitcoin_price[0]
ethereum_price = ethereum_price[0]
ripple_price = ripple_price[0]
substratum_price = substratum_price[0] 
cost = cost[0]
allowance = allowance[0]

#final price of cryptocurrencies in dollars by turning it into floats
bitcoin_price = float(bitcoin_price)
ethereum_price = float(ethereum_price)
ripple_price = float(ripple_price) * bitcoin_price
substratum_price = float(substratum_price) * bitcoin_price
cost = int(cost)
allowance = int(allowance)
        
print("bitcoin:", bitcoin_price)
print("ethereum:", ethereum_price)
print("ripple:", ripple_price)
print("substratum:", substratum_price)