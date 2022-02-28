import requests

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token 9cc1c059bee7ea41a3ce614958f8c9a9ed9a8133'
        }

def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response = requests.get(url,headers=headers)
    return response.json()

def get_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url,headers=headers)
    return response.json()[0]