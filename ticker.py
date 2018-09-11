import requests

ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + '?structure=array'


limit = '20'  # default 100
start = '1'
sort = 'id'
convert = 'USD'

choice = input("Do you want to enter any custom parameters& (y/n): ")

if choice == 'y':
    limit = input("What is the custom limit?")
    start = input("What is  the custom start number?")
    sort = input("What do you want to sort by? ")
    convert = input("What is your local currency?: ")

ticker_url += '&limit=' + limit + '&sort=' + sort + '&start=' + start + '&convert=' + convert

request = requests.get(ticker_url)
results = request.json()

data = results['data']

for currency in data:
    name = currency['name']
    symbol = currency['symbol']
    circulating_supply = currency['circulating_supply']
    total_supply = currency['total_supply']

    quotes = currency['quotes'][convert]
    market_cap = quotes['market_cap']
    price = quotes['price']

    print(name, '->', symbol, circulating_supply, total_supply, market_cap, price)
    print(f'Price of {name} is ${price} ')
