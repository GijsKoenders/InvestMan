from lxml import html
import requests
from time import sleep
import re
from matplotlib import pyplot as plt

bitcoin_historic = []
ethereum_historic = []
ripple_historic = []
substratum_historic = []

bitcoin_list = []
ethereum_list = []
ripple_list = []
substratum_list = []

def webscraper():
    
    """The webscraper calls realtime price information for cryptocurrencies"""
    
    while True:

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
        
        #historic information since session has started, past prices are appended to a list
        bitcoin_historic.append(bitcoin_price)
        ethereum_historic.append(ethereum_price)
        ripple_historic.append(ripple_price)
        substratum_historic.append(substratum_price)
        
        #check for unique values in historic 
        bitcoin_historic_set = set(bitcoin_historic)
        ethereum_historic_set = set(ethereum_historic)
        ripple_historic_set = set(ripple_historic)
        substratum_historic_set = set(substratum_historic)
        
        #initiate self eating graphs when datapoints are equal to 7
        if len(bitcoin_historic_set) == 10 or len(bitcoin_historic) >100:
            bitcoin_historic.pop(0)
        
        if len(ethereum_historic_set) == 10 or len(ethereum_historic) >100:
            ethereum_historic.pop(0)
            
        if len(ripple_historic_set) == 10 or len(ripple_historic) >100:
            ripple_historic.pop(0)
        
        if len(substratum_historic_set) == 10 or len(substratum_historic) >100:
            substratum_historic.pop(0)
        
        #start plotting!
        fig = plt.figure()
        
        #place on canvas of ticker
        axes1 = fig.add_axes([0.1,0.6,0.3,0.3])
        axes2 = fig.add_axes([0.6,0.6,0.3,0.3])
        axes3 = fig.add_axes([0.1,0.1,0.3,0.3])
        axes4 = fig.add_axes([0.6,0.1,0.3,0.3])
        
        #title 
        axes1.set_title("Bitcoin price")
        axes2.set_title("Ethereum price")
        axes3.set_title("Ripple price")
        axes4.set_title("Substratum price")
        
        #xlabel
        axes1.set_xlabel("Iterations")
        axes2.set_xlabel("Iterations")
        axes3.set_xlabel("Iterations")
        axes4.set_xlabel("Iterations")
        
        #ylabel
        axes1.set_ylabel("In Dollars")
        axes2.set_ylabel("In Dollars")
        axes3.set_ylabel("In Dollars")
        axes4.set_ylabel("In Dollars")
        
        #colour of price movement  
        if bitcoin_historic[-1] not in bitcoin_list:
            bitcoin_list.append(bitcoin_historic[-1])
        if ethereum_historic[-1] not in ethereum_list:
            ethereum_list.append(ethereum_historic[-1])
        if ripple_historic[-1] not in ripple_list:
            ripple_list.append(ripple_historic[-1])
        if substratum_historic[-1] not in substratum_list:
            substratum_list.append(substratum_historic[-1])
        
        if len(bitcoin_list) == 1:
            axes1.plot(bitcoin_historic)
        if len(bitcoin_list) >= 2:
            if bitcoin_list[-1] > bitcoin_list[-2]:
                axes1.plot(bitcoin_historic, color = "#00870b")
            elif bitcoin_list[-1] < bitcoin_list[-2]:
                axes1.plot(bitcoin_historic, color = "#ff0000")
        
        if len(ethereum_list) == 1:
            axes2.plot(ethereum_historic)
        if len(ethereum_list) >= 2:
            if ethereum_list[-1] > ethereum_list[-2]:
                axes2.plot(ethereum_historic, color = "#00870b")
            elif ethereum_list[-1] < ethereum_list[-2]:
                axes2.plot(ethereum_historic, color = "#ff0000")
        
        if len(ripple_list) == 1:
            axes3.plot(ripple_historic)
        if len(ripple_list) >= 2:
            if ripple_list[-1] > ripple_list[-2]:
                axes3.plot(ripple_historic, color = "#00870b")
            elif ripple_list[-1] < ripple_list[-2]:
                axes3.plot(ripple_historic, color = "#ff0000")                   
        
        if len(substratum_list) == 1:
            axes4.plot(substratum_historic)
        if len(substratum_list) >= 2:
            if substratum_list[-1] > substratum_list[-2]:
                axes4.plot(substratum_historic, color = "#00870b")
            elif substratum_list[-1] < substratum_list[-2]:
                axes4.plot(substratum_historic, color = "#ff0000")    
        
        #no scientific notation possible 
        axes1.ticklabel_format(useOffset=False, style='plain')
        axes2.ticklabel_format(useOffset=False, style='plain')
        axes3.ticklabel_format(useOffset=False, style='plain')
        axes4.ticklabel_format(useOffset=False, style='plain')
        
        #print canvas!
       
        plt.show()
        
        #information on how many times we can call the webscraper 
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

webscraper()