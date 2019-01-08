from lxml import html
import requests
from time import sleep
import re

while True:

    scrape = requests.get("https://api.cryptowat.ch/markets/prices")
    scrape_content = html.fromstring(scrape.content)
    
    scrape_link = scrape_content.xpath("text()")
    scrape_link = scrape_link[0]
    
    bitcoin_ticker = re.findall(r'coinbase-pro:btcusd":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:btcusd":+\d+', scrape_link)
    ethereum_ticker = re.findall(r'coinbase-pro:ethusd":+\d+\.+\d+', scrape_link) or re.findall(r'coinbase-pro:ethusd":+\d+', scrape_link)
    ripple_ticker = re.findall(r'binance:xrpbtc":+\d+\.+\d+', scrape_link) 
    substratum_ticker = re.findall(r'binance:subbtc":+\d+\.+\d+', scrape_link) 
    cost = re.findall(r'cost":+\d+', scrape_link)    
    allowance = re.findall(r'remaining":+\d+', scrape_link)

    bitcoin_price = re.findall(r'\d+\.+\d+', bitcoin_ticker[0]) or re.findall(r'\d+', bitcoin_ticker[0])
    ethereum_price = re.findall(r'\d+\.+\d+', ethereum_ticker[0]) or re.findall(r'\d+', ethereum_ticker[0])
    ripple_price = re.findall(r'\d+\.+\d+', ripple_ticker[0]) or re.findall(r'\d+', ripple_ticker[0])
    substratum_price = re.findall(r'\d+\.+\d+', substratum_ticker[0]) or re.findall(r'\d+', substratum_ticker[0])
    cost = re.findall(r'\d+', cost[0])
    allowance = re.findall(r'\d+', allowance[0])

    bitcoin_price = bitcoin_price[0]
    ethereum_price = ethereum_price[0]
    ripple_price = ripple_price[0]
    substratum_price = substratum_price[0] 
    cost = cost[0]
    allowance = allowance[0]

    bitcoin_price = float(bitcoin_price)
    ethereum_price = float(ethereum_price)
    ripple_price = float(ripple_price) * bitcoin_price
    substratum_price = float(substratum_price) * bitcoin_price
    cost = int(cost)
    allowance = int(allowance)

    if allowance < 800000000:
        print("Bitcoin:", bitcoin_price)
        print("Ethereum:", ethereum_price)
        print("Ripple:", ripple_price)
        print("Substratum:", substratum_price)
        print("CPU cost:", cost)
        print("Current allowance:", allowance)
        print("Prices update every 5 seconds")
        print("")
        sleep(5)
        
    if allowance < 2800000000:
        print("Bitcoin:", bitcoin_price)
        print("Ethereum:", ethereum_price)
        print("Ripple:", ripple_price)
        print("Substratum:", substratum_price)
        print("CPU cost:", cost)
        print("Current allowance:", allowance)
        print("Prices update every 3 seconds")
        print("")
        sleep(3)
        
    if allowance < 8000000000:
        print("Bitcoin:", bitcoin_price)
        print("Ethereum:", ethereum_price)
        print("Ripple:", ripple_price)
        print("Substratum:", substratum_price)
        print("CPU cost:", cost)
        print("Current allowance:", allowance)
        print("Prices update every 0.3 seconds")
        print("")
        sleep(0.3)
    
    if allowance == 0 or allowance < 0: 
        print("No new requests possible, wait till the hour has passed to start fresh!")
        sleep(60)
