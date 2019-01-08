from lxml import html
import requests
from time import sleep
import re

def bitcoin_sleeper():
    bitcoin_page = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/btcusd/price")
    bitcoin_content = html.fromstring(bitcoin_page.content)
    
    bitcoin_link = bitcoin_content.xpath("text()")
    bitcoin_link = bitcoin_link[0]
    bitcoin_link = re.findall(r"[\w']+", bitcoin_link)

    allowance = bitcoin_link[-1]
    allowance = float(allowance)
    
    if allowance <= 800000000:
        print("Refreshing data every 30 seconds")
        print("")
        sleep(30)
    if allowance <= 2800000000:
        print("Refreshing data every 10 seconds")
        print("")
        sleep(10)
    if allowance <= 8000000000:
        print("Refreshing data every 3 seconds")
        print("")
        sleep(3)
    return 

def bitcoin_printer():
    bitcoin_dollar = bitcoin_link[2]
    bitcoin_cents = bitcoin_link[3]
    cost = bitcoin_link[-3]
    bitcoin_float = bitcoin_dollar+"."+bitcoin_cents
    
    if bitcoin_cents.isdigit():
        bitcoin_float = float(bitcoin_float)
        print("Bitcoin:", bitcoin_float)
        print("The cost of getting data:", cost)
        print("Allowance remaining:", allowance)
        bitcoin_sleeper()
    
    else:
        bitcoin_dollar = float(bitcoin_dollar)
        print("Bitcoin:", bitcoin_dollar)
        print("The cost of getting data:", cost)
        print("Allowance remaining:", allowance)
        bitcoin_sleeper()
    return

def ethereum_sleeper():
    ethereum_page = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/ethusd/price")
    ethereum_content = html.fromstring(ethereum_page.content)
    
    ethereum_link = ethereum_content.xpath("text()")
    ethereum_link = ethereum_link[0]
    ethereum_link = re.findall(r"[\w']+", ethereum_link)

    allowance = ethereum_link[-1]
    allowance = float(allowance)
    
    if allowance <= 800000000:
        print("Refreshing data every 30 seconds")
        print("")
        sleep(30)
    if allowance <= 2800000000:
        print("Refreshing data every 10 seconds")
        print("")
        sleep(10)
    if allowance <= 8000000000:
        print("Refreshing data every 3 seconds")
        print("")
        sleep(3)
    return

def ethereum_printer():
    ethereum_dollar = ethereum_link[2]
    ethereum_cents = ethereum_link[3]
    cost = ethereum_link[-3]
    ethereum_float = ethereum_dollar+"."+ethereum_cents
    
    if ethereum_cents.isdigit():
        ethereum_float = float(ethereum_float)
        print("Ethereum:", ethereum_float)
        print("The cost of getting data:", cost)
        print("Allowance remaining:", allowance)
        ethereum_sleeper()
    
    else:
        ethereum_dollar = float(ethereum_dollar)
        print("Ethereum:", ethereum_dollar)
        print("The cost of getting data:", cost)
        print("Allowance remaining:", allowance)
        ethereum_sleeper()
    return

while True:
    bitcoin_page = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/btcusd/price")
    bitcoin_content = html.fromstring(bitcoin_page.content)
    
    bitcoin_link = bitcoin_content.xpath("text()")
    bitcoin_link = bitcoin_link[0]
    bitcoin_link = re.findall(r"[\w']+", bitcoin_link)

    bitcoin_dollar = bitcoin_link[2]
    bitcoin_cents = bitcoin_link[3]
    allowance = bitcoin_link[-1]
    cost = bitcoin_link[-3]
    bitcoin_float = bitcoin_dollar+"."+bitcoin_cents

    ethereum_page = requests.get("https://api.cryptowat.ch/markets/coinbase-pro/ethusd/price")
    ethereum_content = html.fromstring(ethereum_page.content)
    
    ethereum_link = ethereum_content.xpath("text()")
    ethereum_link = ethereum_link[0]
    ethereum_link = re.findall(r"[\w']+", ethereum_link)

    ethereum_dollar = ethereum_link[2]
    ethereum_cents = ethereum_link[3]
    allowance = ethereum_link[-1]
    cost = ethereum_link[-3]
    ethereum_float = ethereum_dollar+"."+ethereum_cents

    ethereum_printer()

    bitcoin_printer()
    