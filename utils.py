import requests
from streamlit import secrets

def get_stocks(stock):
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={stock}&apikey=secrets['ALPHA_VANTAGE_API_KEY']"
    r = requests.get(url)
    datas = r.json()
    
    return datas["bestMatches"]