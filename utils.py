import requests


def get_stocks(stock):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={stock}&apikey=F28WJE7XJWJJWQJC'
    r = requests.get(url)
    datas = r.json()
    
    return datas["bestMatches"]