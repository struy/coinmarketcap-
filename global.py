import requests
from datetime import datetime
# import json

currency = 'UAH'
global_url = 'https://api.coinmarketcap.com/v2/global/?convert=' + currency

request = requests.get(global_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))
active_currencies = results['data']['active_cryptocurrencies']
global_cap = int(results['data']['quotes'][currency]['total_market_cap'])
last_updated = datetime.fromtimestamp(results['data']['last_updated']).strftime('%B %d,%Y at %I:%M')

print(('Active currencies: {:,}, the global cap of all cryptos is ({currency}) {:,}').format(active_currencies, global_cap, currency=currency))
print('This information was last updated on %s' % last_updated)
