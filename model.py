import requests
import pandas as pd

# define this function to get user input for a time frame
def get_function(function):
    if 'intraday' in (x.lower):
        return 'TIME_SERIES_INTRADAY'
    elif 'intraday extended' in (x.lower):
        return 'TIME_SERIES_INTRADAY_EXTENDED'
    elif 'daily' in (x.lower):
      return 'TIME_SERIES_DAILY'
    elif 'weekly' in (x.lower):
      return 'TIME_SERIES_WEEKLY'
    elif 'monthly' in (x.lower):
      return 'TIME_SERIES_MONTHLY'
    else:
      return (x.UPPER)
  
#define this function to get user input for a symbol
#def get_symbol(symbol):
#
#
#
#
#.   return symbol

#define this function to get user input for interval
# def get_interval(interval):
#
#
#
#
#
#    return interval
 
symbol=input('Get Symbol')
interval=input('Get interval')
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?'+'function={}'+'&symbol={}'+'&interval={}'+'&apikey=4BB9V8QME0K5H135'.format(function,symbol,interval)
r = requests.get(url)
data = r.json()
df=pd.json_normalize(data)
